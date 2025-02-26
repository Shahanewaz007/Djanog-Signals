from django.db import models

class User(models.Model):  
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
