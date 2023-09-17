# scraper/cron.py

from django_cron import CronJobBase, Schedule
from .property_scrapper import scrape_and_save_property_data

class MyCronJob(CronJobBase):
    RUN_EVERY_12_HOURS = 720 

    schedule = Schedule(run_every_mins=RUN_EVERY_12_HOURS)
    code = 'scrapper.My_Cron_Job'

    def do(self):
        scrape_and_save_property_data()
