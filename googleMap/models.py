# from django.db import models
# import datetime
# # Create your models here.

# class SaveUserAddress(models.Model):
#     addressType = models.CharField(max_length=100)
#     #user_id = models.IntegerField()
#     email = models.EmailField(max_length=128, verbose_name="Email")
#     address = models.CharField(max_length=100)
#     lat = models.CharField(max_length=100)
#     lang = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)

#     def __int__(self):
#         return self.user_id