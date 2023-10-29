from django.shortcuts import render
from django.core.cache import cache
from django.views.decorators.cache import cache_page
import requests

# from django.core.mail import EmailMessage, BadHeaderError
# from templated_mail.mail import BaseEmailMessage
# from .task import notify_customers

@cache_page(5*60)
def say_hello(request):
    response = requests.get('http://httpbin.org/delay/2')
    data = response.json()

    return render(request, 'hello.html', {'name': data})






# def say_hello(request):
#     notify_customers.delay('Hello')
#     # try:
#     #     message = BaseEmailMessage(
#     #         template_name='emails/mail.html',
#     #         context = {
#     #             'name' : 'Mehfooz',
#     #         }
#     #     )
#     #     message.send(['mehfooz.connect@gmail.com'])

#     # except BadHeaderError:
#     #     pass

#     return render(request, 'hello.html', {'name': 'Mosh'})