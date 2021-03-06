from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from performances.models import Class, Institution, Performance

from .managers import CustomUserManager


# Create your models here.
class CustomUser(AbstractUser):
    """
    Defines the primary attributes of all users.
    """
    ROLES = (
        ('TEACHER', 'Teacher'),
        ('ADJUDICATOR', 'Adjudicator'),
        ('INDEPENDENT_PERFORMER', 'Independent Performer'),
        ('DEPENDENT_PERFORMER', 'Dependent Performer'),
        ('SPONSOR', 'Sponsor'),
        ('TRAINER', 'Trainer'),
        ('HEAD_OF_INSTITUTION', 'Head of Institution')
    )

    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30)
    middle_name = models.CharField(_('middle name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30)
    is_active = models.BooleanField(_('active'), default=True)
    role = models.CharField(max_length=50, choices=ROLES, default='TEACHER')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS: list = []

    def get_long_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s %s' % (
            self.first_name,
            self.middle_name,
            self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def __str__(self):
        return self.email


class HeadOfInstitution(models.Model):
    """
    Head of an institution participating in the Festival.
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class TeacherProfile(models.Model):
    """
    Teacher responsible for a set of performances in an institution
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    institution = models.ForeignKey(
        to=Institution,
        on_delete=models.CASCADE,
        null=True)
    performances = models.ManyToManyField(
        Performance,
        related_name="performances_under_care")

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'


class IndependentPerformerProfile(models.Model):
    """
    These are performers who pay for themselves.
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    institution = models.ForeignKey(
        to=Institution,
        on_delete=models.CASCADE,
        null=True)
    performances = models.ManyToManyField(
        Performance,
        related_name="performing_in")

    class Meta:
        verbose_name = 'independent performer'
        verbose_name_plural = 'independent performers'


class SponsorProfile(models.Model):
    """
    Defines  financial sponsors for  underage performers.
    """
    PAYMENT_METHODS = (
        ("PAYPAL", 'Paypal'),
        ("MPESA", 'Mpesa'))

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_METHODS,
        default="MPESA")

    class Meta:
        verbose_name = 'sponsor'
        verbose_name_plural = 'sponsors'


class DependentPerformerProfile(models.Model):
    """
    Defines school going performers who have to rely on  teachers
    to register them, train them and generally be responsible for their performance groups.
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    institution = models.ForeignKey(
        to=Institution,
        on_delete=models.CASCADE,
        null=True)
    performance = models.ManyToManyField(Performance)

    class Meta:
        verbose_name = 'dependent performer'
        verbose_name_plural = 'dependent performers'


class AdjudicatorProfile(models.Model):
    """
    Defines a judge of performances in the Festival.
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    # institution = models.ForeignKey
    # adjudication_levels = models.ManyToManyField

    class Meta:
        verbose_name = 'adjudicator'
        verbose_name_plural = 'adjudicators'
