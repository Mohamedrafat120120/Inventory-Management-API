from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,phone_number,is_staff,password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email=self.normalize_email(email), password=password,
            first_name=first_name,
            last_name =last_name ,
            phone_number=phone_number,
            is_staff=is_staff,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email,first_name,last_name,phone_number,is_staff,password):
        user = self.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name =last_name ,
            phone_number=phone_number,
            is_staff=is_staff,
            
        )
        
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number=models.CharField(max_length=11,blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['first_name','last_name','phone_number','is_staff']
    def __str__(self):
        return self.email