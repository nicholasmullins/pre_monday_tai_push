
import logging
import time

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    driver.switch_to_window_by_title("AI-Driven Testing: A New Era of Test Automation")
    context.get_all_elements()