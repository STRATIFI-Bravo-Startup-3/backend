from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from rest_framework.authtoken.models import Token
from django.conf import settings

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        EMPLOYEE = "EMPLOYEE", "Employee"
        INFLUENCER = "INFLUENCER", "Influencer"
        BRAND = "BRAND", "Brand"

    base_role = Role.INFLUENCER

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)
    
    def __str__(self) :
        return self.email

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class EmployeeManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.EMPLOYEE)

class Employee(User):

    base_role = User.Role.EMPLOYEE

    employee = EmployeeManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for employees of stratifi"


class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.IntegerField(null=True, blank=True)
    full_name = models.CharField(max_length=200, null=True, blank=True)
    position = models.CharField(max_length=200, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    tik_tok_url = models.URLField(null=True, blank=True)


@receiver(post_save, sender=Employee)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "EMPLOYEE":
        EmployeeProfile.objects.create(user=instance)


class InfluencerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.INFLUENCER)


class Influencer(User):

    base_role = User.Role.INFLUENCER

    influencer = InfluencerManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Influencers"


@receiver(post_save, sender=Influencer)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "INFLUENCER":
        InfluencerProfile.objects.create(user=instance)


class InfluencerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    influencer_id = models.IntegerField(null=True, blank=True)
    full_name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    portfolio = models.TextField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    linkedin_followers = models.IntegerField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    facebook_followers = models.IntegerField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    instagram_followers = models.IntegerField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    twitter_followers = models.IntegerField(null=True, blank=True)
    tik_tok_url = models.URLField(null=True, blank=True)
    tit_tok_followers = models.IntegerField(null=True, blank=True)


class BrandManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.BRAND)


class Brand(User):

    base_role = User.Role.BRAND

    brand = BrandManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for brands"


class BrandProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    brand_id = models.IntegerField(null=True, blank=True)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    company_size = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    linkedin_followers = models.IntegerField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    facebook_followers = models.IntegerField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    instagram_followers = models.IntegerField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    twitter_followers = models.IntegerField(null=True, blank=True)
    tik_tok_url = models.URLField(null=True, blank=True)
    tit_tok_followers = models.IntegerField(null=True, blank=True)


@receiver(post_save, sender=Brand)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "BRAND":
        BrandProfile.objects.create(user=instance)