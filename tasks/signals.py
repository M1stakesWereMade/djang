from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task
from django.core.mail import send_mail

@receiver(post_save, sender=Task)
def notify_users(sender, instance, created, **kwargs):
    if created:
        subject = 'Новая задача создана'
        message = f'Задача "{instance.title}" была создана.'
        recipient_list = [user.email for user in instance.project.users.all()]  # Предполагается, что у проекта есть связанные пользователи
        send_mail(subject, message, 'admin@example.com', recipient_list)
