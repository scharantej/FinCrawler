## Structure: Crawling Financial Reports of Chinese A-Share Listed Companies

**HTML Files**:
1. **Homepage:** (home.html)
   - Provides a brief introduction to the application and its functionality.
   - Includes a link to the list of financial reports page.

2. **List of Financial Reports:** (reports.html)
   - Displays a table with all the available financial reports, including company name, report date, and a link to the report file.
   - Include a search bar to filter the reports by company name.
   - Have a button to initiate the crawling process.

3. **Financial Report:** (report.html)
   - Displays the full financial report for the selected company.
   - Displays various sections of the report using separate HTML elements.
   - Include a button to download the report in PDF format.

4. **Crawling in Progress:** (crawling.html)
   - Displays a progress bar and status messages during the crawling process.
   - Updates the status as the crawler downloads and parses the financial reports.

**Routes**:
1. **Homepage:** ('/')
   - Serves the homepage (home.html).

2. **Financial Report List:** ('/reports')
   - Generates the list of financial reports and serves it using the reports.html template.

3. **Financial Report Detail:** ('/report/<report_id>')
   - Fetches the financial report with the given ID from the database.
   - Serves the report using the report.html template.

4. **Crawling:** ('/crawling')
   - Initiates the crawling process by creating a new job in a background thread.
   - Serves the crawling.html page to display the progress.

5. **Download Report PDF:** ('/download/<report_id>')
   - Generates a PDF file from the specified report and returns it as a response.

## Implementation Notes
- Use Flask's Jinja2 templating system to render the HTML pages dynamically.
- Store the financial reports in a database to allow searching and filtering.
- Utilize a background task queue system (such as Celery) to handle the crawling process asynchronously.
- Consider adding a caching mechanism to improve the performance of report retrieval.
- Employ error handling and logging to ensure a stable and resilient application.