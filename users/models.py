from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser,PermissionsMixin)
from django.utils.translation import gettext as _


USER_TYPES = (
    ("AUTHOR", "AUTHOR"),
    ("VENDOR", "VENDOR"),
    ("CUSTOMER", "CUSTOMER"),
    ("SUB_ADMIN", "SUB_ADMIN"),
    ("SUPER_ADMIN", "SUPER_ADMIN"),
)


class UserManager(BaseUserManager):
    def create_user(self, firstname, lastname, email, password=None):
        if firstname is None:
            raise TypeError('User shold have a firstname')
        if lastname is None:
            raise TypeError('User shold have a lastname')
        if email is None:
            raise TypeError('User shold have a email')
        
        email = str(email).lower()
        user = self.model(
            firstname = firstname,
            lastname  = lastname,
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, firstname, lastname, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(
            email=self.normalize_email(email),
            firstname=firstname,
            lastname=lastname,
            password=password,
        )

        user.is_superuser = True
        user.is_admin = True
        user.is_active = True
        user.is_verified = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    role = models.CharField(_("role"), max_length=50, choices=USER_TYPES)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']

    objects = UserManager()

    def __str__(self):
        return self.email

    