import os

from celery import Celery
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from users.models import User
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Biotech.settings')

app = Celery('Biotech')

app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()


@app.task()
def send_otp_email(user_id):
    user = User.objects.get(id=user_id)
    otp_code = default_token_generator.make_token(user)
    user.confirmation_code = otp_code
    user.save()
    send_mail(
        'Ваш OTP код',
        f'Ваш OTP код это: {otp_code}',
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )
