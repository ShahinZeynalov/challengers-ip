import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User

# from utilities.utils import get_filename, rotate_image
#
#
# @receiver(post_save, sender=User, dispatch_uid="update_image_profile")
# def update_image(sender, instance, **kwargs):
#   if instance.profile_image:
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     fullpath = BASE_DIR + instance.profile_image.url
#     rotate_image(fullpath)
