
import logging
import time

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    driver.switch_to_window_by_title("AI and the Future of Testing | Centercode")
    context.get_all_elements()