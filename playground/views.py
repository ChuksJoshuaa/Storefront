from django.shortcuts import render
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers


def say_hello(request):
    notify_customers.delay('Hello')
    return render(request, 'hello.html', {'name': 'Mosh'})


def say_bye(request):
    try:
        message = EmailMessage('subject', 'message',
                               'from@moshbuy.com', ['admin@gmail.com'])
        message.attach_file('media/store/baby.jpg')
        message.send()
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Mosh'})


def say_yes(request):
    try:
        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context={'name': 'Chuks'}
        )
        message.send(['admin@gmail.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Mosh'})

# celery commands
# before that run the docker command to connect to redis
# docker run -d -p 6379:6379 redis
# after that python -m pip install redis
# open another terminal to run the manage.py runserver
# then run the below command in another terminal
# celery -A <project> worker -l info -P gevent
# open another terminal to run this command
# celery -A <project> beat
# python -m pip install flower
# celery -A <project> flower
# access the page

# incase that one no work
# pip install eventlet
# celery - A <project> worker -l info -P eventlet

# how to test specify the stuff to be tested
# pytest store/tests/test_collections.py::TestCreateCollection
# pytest -k anonymous

# we use @pytest.mark.skip to skip some tests we dont want, and let it be at the top like a decorator.

# Also we use ptw to run continous test
