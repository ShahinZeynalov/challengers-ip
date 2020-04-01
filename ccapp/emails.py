from django.core.mail import send_mail, send_mail
from django.conf import settings

def send_feedback_email(sender_email, sender_name):
    subject = 'Mesajını aldım'
    message = 'Salam, dəyərli ' + str(sender_name) + '. \nMesajını aldım. Ən qısa zamanda cavablandıracam. \nTəşəkkür edirəm.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [sender_email]
    send_mail(subject, message, from_email, recipient_list)
