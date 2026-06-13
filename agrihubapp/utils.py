# agrihubapp/utils.py (or notifications.py)
from django.core.mail import send_mail
from django.conf import settings

def notify_all_users(subject, message, link, recipients):
    """
    Send an email notification to a list of recipients.
    - subject: Email subject line
    - message: Short summary or teaser text
    - link: Full URL to continue reading
    - recipients: List of email addresses
    """
    full_message = f"{message}\n\nContinue reading: {link}"
    send_mail(
        subject,
        full_message,
        settings.DEFAULT_FROM_EMAIL,
        recipients,
        fail_silently=False,
    )
