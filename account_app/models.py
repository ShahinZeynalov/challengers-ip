from django.db import models
from dashboard_app.models import Badge
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser , BaseUserManager

GENDER_CHOICE = (
    (-1,'unselected'),
    (0,'male'),
    (1,'female'),
)
class User(AbstractUser):
    gender = models.IntegerField(choices=GENDER_CHOICE,default=-1)
    date_of_birth = models.DateField(null=True, blank= True)
    profile_image = models.ImageField(upload_to='user/images', null=True,blank=True)
    email = models.EmailField(_('email address'), unique=True)
    badges = models.ManyToManyField(Badge,related_name='users', blank=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name']

    def get_username(self):
        return self.email
