from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.urls import reverse
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):
    """
    Used for AUTH_USER_MODEL
    """
    username = models.CharField(max_length=16, unique=True, validators=[ASCIIUsernameValidator()])
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email',]
    objects = UserManager()

    def __str__(self):
        return f'User {self.username}'

    def get_absolute_url(self):
        """
        Returns the UserPostsView of the user
        """
        return reverse('posts:user_posts', kwargs={'username':self.username})

    @property
    def name(self):
        return self.profile.name


class Profile(models.Model):
    """
    Profile for individual users
    """
    MALE = 'm'
    FEMALE = 'f'
    OTHER = 'o'
    NA = ''
    GENDERS = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
        (NA, 'Prefer not to say'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    gender = models.CharField(max_length=1, blank=True, choices=GENDERS)
    birthday = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'Profile for {self.user}'

    @property
    def age(self):
        """
        Return the age of the profile if birthday is set, None otherwise
        """
        if self.birthday is None:
            return None
        else:
            today = timezone.now()
            return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
