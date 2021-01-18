import logging
import time
import os

log = logging.getLogger(__name__)

MAX_SWIPES = 10


def run(context):
    link = False
    attempts = 0

    link = element_exists(context, 'lnk_test_ai')
    
    while not link and attempts <= MAX_SWIPES:
        attempts += 1
        context.perform_gesture('swipe_up', '')
        link = element_exists(context, 'lnk_test_ai')

    context.verify(['lnk_test_ai'])


def element_exists(context, label):
    labels_per_elem = context.find_elements_with_label(label)
    return labels_per_elem and len(labels_per_elem.keys()) > 0