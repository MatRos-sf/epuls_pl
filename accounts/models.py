from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

#admin, ma@wp.pl, admin

class MyAccountManager(BaseUserManager):
    def create_user(self, username, email,password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("User must have an username")

        user = self.model(
            email = self.normalize_email(email),
            username = username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

class PersonalDetails(models.Model):

    height = models.CharField(max_length=50, blank=True, default="")
    weight = models.CharField(max_length=50, blank=True, default="")
    marital_status = models.CharField(max_length=50, blank=True, default="")
    dish = models.CharField(max_length=50, blank=True, default="")
    movie = models.CharField(max_length=50, blank=True, default="")
    song = models.CharField(max_length=50, blank=True, default="")



class Puls(models.Model):

    for_login = models.IntegerField(default=5, blank=True)

    def __str__(self):
        return str(self.for_login)

class Account(AbstractBaseUser):

    SEX = [
        ('1', 'mężczyzna'),
        ('2', 'kobieta')
    ]

    email = models.EmailField(unique=True, verbose_name='email')
    username = models.CharField(unique=True,  max_length=40, verbose_name='username')
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    sex = models.CharField(max_length=1, choices=SEX, blank=True, null=True)

    puls = models.OneToOneField(Puls, on_delete=models.CASCADE)
    personal_detail = models.OneToOneField(PersonalDetails, on_delete=models.CASCADE)




    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']          #co jest nam potrzebne

    objects = MyAccountManager()


    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        self.is_admin

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        if self.pk is None:
            #self.points = Points.objects.create()
            # create model with personal date
            self.personal_detail = PersonalDetails.objects.create()
            #create model with puls
            self.puls = Puls.objects.create()
        super().save(*args, **kwargs)