from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
)
from django.core.validators import RegexValidator
from django.db.models.signals import post_save

USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'


class MyUserManager(BaseUserManager):
	def create_user(self, email,  password=None):
		"""
		Creates and saves a User with the given email, date of
		birth and password.
		"""
		if not email:
			raise ValueError('Users must have an email address')

		
		email = self.normalize_email(email)
		user = self.model(email=email)
		user.is_active = True
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		"""
		Creates and saves a superuser with the given email and password.
		"""
		user = self.create_user(
			email,
			password=password,
		)
		user.is_admin = True
		user.is_staff = True
		user.save(using=self._db)
		return user


class MyUser(AbstractBaseUser):
	# username = models.CharField(
	# 			max_length=120, 
	# 			validators=[
	# 			RegexValidator(
	# 					regex= USERNAME_REGEX,
	# 					message = 'Username must be Alphanumeric',
	# 					code = 'invalide username'
	# 				)], 
	# 			unique = True, 
	# 		)
	email = models.EmailField(
		verbose_name='email address',
		max_length=255,
		unique=True,
	)


	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)

	objects = MyUserManager()

	USERNAME_FIELD = 'email'
	# REQUIRED_FIELDS = ['email']

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True


class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=120, null=True, blank=True)
	last_name = models.CharField(max_length=120, null=True, blank=True)
	
	def __str__(self):
		return str(self.user.email)

def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
	if created:
		try:
			Profile.objects.create(user=instance)
		except:
			pass


post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)

