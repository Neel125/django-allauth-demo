from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.
class UserManager(BaseUserManager):
    """
    Custom user manger class to create user
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save the New User
        :param email: email address of user
        :param password: password of user
        :param extra_fields: extra keyword arguments of user field
        :return: user object
        """
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        create super user
        :param email: email adderess of super user
        :param password: password of super user
        :return: super user object
        """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User Model that supports using email instead of username
    """
    id = models.AutoField(primary_key=True, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.username
