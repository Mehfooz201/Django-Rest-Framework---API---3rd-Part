from time import sleep
# from storefront.celery import celery
from celery import shared_task


@shared_task
def notify_customers(message):
    print('Sending 10k emails ... ')
    print(message)
    sleep(10)
    print('Emails were succesffuly sent !')