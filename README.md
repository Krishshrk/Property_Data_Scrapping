# Property Data Scraping

This Django project schedules and manages a property data scraping script for the 99acres website. It scrapes essential property details such as property name, cost, type, area, and individual property links. The scraped data is stored in a database and can be scheduled to run twice daily for specific cities and localities using Django's cron job management.

## Project Structure

The project is structured as follows:

- `scrappingtool/`: The Django project directory.
- `scraper/`: The Django app for property data scraping.
  - `models.py`: Defines the database models.
  - `scraper.py`: Contains the scraping script.
  - `cron.py`: Defines the Django cron job for scheduled scraping.
- `scrappingtool/settings.py`: Django project settings.
- `README.md`: This documentation file.

## Installation and Steps to follow

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/property-scraper-project.git
   cd property-scraper-project ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate 

3. Install project dependencies

   ```bash
   pip install -r requirements.txt 

4. Configure the Django project settings in scrappingtool/settings.py. Ensure the database settings and other configurations are properly set up.

5. Run database migrations

   ```bash
   python manage.py makemigrations
   python manage.py migrate 

6. Start the cron job using the following command:

   ```bash
   python manage.py runcrons

7. Start the Django development server

   ```bash
   python manage.py runserver

8. Access the admin panel at http://localhost:8000/admin/ to manage scraped property data

9. Sample output : https://docs.google.com/document/d/1gQ2PW_1KQBZDJkldhzEAhD8jQpMG9f4j/edit?usp=sharing&ouid=107818416453793624005&rtpof=true&sd=true
