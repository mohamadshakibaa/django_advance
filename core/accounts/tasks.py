from celery import shared_task
from time import sleep


@shared_task
def sending_email():
    sleep(5)
    print("done sending email")