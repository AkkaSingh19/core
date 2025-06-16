from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_welcome_email(user_email):
    subject = "Welcome to our website!"
    message = "Thank you for registering, and we hope you enjoy your stay."
    from_email = "your_email@example.com"
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)
