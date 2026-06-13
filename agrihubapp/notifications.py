from django.core.mail import send_mail
from django.conf import settings

def notify_all_users(subject, message, link, recipients):
    full_message = f"{message}\n\nContinue reading: {link}"
    send_mail(
        subject,
        full_message,
        settings.DEFAULT_FROM_EMAIL,
        recipients,
        fail_silently=False,
    )
