from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

#this is for superadmin

class MyAccountManager(BaseUserManager):
    #this is for creating normal user
    def create_user(self,first_name,last_name,username,email,password):
        if not email:
            raise ValueError("User must have an email address")

        if not username:
            raise ValueError("User must have an username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self.db)
        return user
    #this is for creting super user
    def create_superuser(self,first_name,last_name,email,username,password):
       
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self.db)
        return user


#this is for account model

class Account(AbstractBaseUser):
    #this is account
    first_name  =models.CharField(max_length=50)
    last_name   =models.CharField(max_length=50)
    username    =models.CharField(max_length=50,unique=True)
    email       =models.EmailField(max_length=100,unique=True)
    phone_number=models.CharField(max_length=50)

    #required fields when we creating custom user model
    date_joined     =models.DateTimeField(auto_now_add=True)
    last_login      =models.DateTimeField(auto_now_add=True)
    is_admin        =models.BooleanField(default=False)
    is_staff        =models.BooleanField(default=False)
    is_active       =models.BooleanField(default=False)
    is_superadmin   =models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name']

    #we need to tell this  account we are using MyAccountManager for all thse operations
    objects=MyAccountManager()

    def __str__(self):
        return self.email

#other mandatoryy methods these are for permissions

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

    

#last goto setings.py
# we are usiing custom user model so tell to settings
