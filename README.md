# web-scraping

Basics of using glassdoors api to scrape data about jobs progression

Before you start, set your enviornment variables in terminal:

	$ export GLASSDOOR_API_ID="YOUR_API_ID"

	$ export GLASSDOOR_API_KEY="YOUR_API_KEY"

Key features: 

	Job Titles: array of strings. include titles of jobs to be run.

	Most frequent vs. Highest salary: in get_data function, choose if you want to return data based on highest median salary or most likely career projection based on statistics.

	Number of steps into career: some career titles, "director," may not result in a career projection result.

