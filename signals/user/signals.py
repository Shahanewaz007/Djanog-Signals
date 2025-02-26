from django.dispatch import Signal, receiver
from django.core.mail import send_mail
from .models import Profile

user_registered = Signal()

@receiver(user_registered)
def handle_user_registration(sender, user, request, **kwargs):
    

    Profile.objects.create(user=user)


    send_mail(
        subject=f"Welcome, {user.username}!",
        message="Thanks for joining our platform!",
        from_email="example@gmail.com",
        recipient_list=[user.email],
        fail_silently=True,
    )
