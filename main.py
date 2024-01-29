
from flask import Flask, redirect, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reports.db'
db = SQLAlchemy(app)

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(255))
    report_date = db.Column(db.Date)
    report_file = db.Column(db.String(255))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/reports')
def reports():
    reports = Report.query.all()
    return render_template('reports.html', reports=reports)

@app.route('/report/<int:report_id>')
def report(report_id):
    report = Report.query.get_or_404(report_id)
    return render_template('report.html', report=report)

@app.route('/crawling', methods=['GET', 'POST'])
def crawling():
    if request.method == 'POST':
        # Initiate crawling process in a background thread
        import crawler
        crawler.crawl_reports()
        return redirect(url_for('crawling'))
    return render_template('crawling.html')

@app.route('/download/<int:report_id>')
def download(report_id):
    report = Report.query.get_or_404(report_id)
    file_path = os.path.join('reports', report.report_file)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
