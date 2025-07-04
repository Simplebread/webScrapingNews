# INSTRUCTIONS TO RUN
# RUN THIS TO EXECUTE CRON JOB
# */2 * * * * /usr/bin/python3 /path/to/your/run_scraper.py

# scheduler.py
import schedule
import time
import subprocess
import logging
from error_log import setup_logger

# Setup logger for debugging
logger = setup_logger(__name__)
logger.info("Running scheduler for automation.")

# Setup logging
logging.basicConfig(filename="scheduler.log", level=logging.INFO)

def job():
    logging.info("Running run_scraper.py...")
    try:
        subprocess.run(["python3", "run_scraper.py"], check=True)
        # Debugging
        logging.info("run_scraper.py executed successfully.")
    except subprocess.CalledProcessError as e:
        # Debugging
        logging.error(f"run_scraper.py failed: {e}")

# Schedule it: every hour (change to your needs)
schedule.every(2).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
