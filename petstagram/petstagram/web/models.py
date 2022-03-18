import datetime
from enum import unique

from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinLengthValidator

from petstagram.accounts.models import PetstagramUser
from petstagram.web.validators import validate_only_letters, validate_file_max_size_in_mb

UserModel = get_user_model()


class Profile(models.Model):
    # Constants
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'
    # GENDERS = [
    #     ('Male', 'Male'),
    #     ('Female', 'Female'),
    #     ('Do not show', 'Do not show')
    # ] ^ same as v
    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]
    # Fields
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )
    picture = models.URLField()

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True,
        default=DO_NOT_SHOW,
    )
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )


# if value == 'Male': => Bad
# if value == Profile.MALE => Good


class Pet(models.Model):
    # Constants
    CAT = "Cat"
    DOG = "Dog"
    BUNNY = "Bunny"
    PARROT = "Parrot"
    FISH = "Fish"
    OTHER = "Other"

    TYPES = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]
    # TYPES = ((x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)), not a tuple comprehension, generator
    NAME_MAX_LENGTH = 30

    MIN_DATE = datetime.date(1920, 1, 1)

    # Fields(Columns)
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
        validators=(
            # MinDateValidator(),
        )
    )

    # One-to-one relations

    # One-to-many relations
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    # Many-to-many relations

    # Properties

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    # Methods

    # dunder methods

    # Meta
    class Meta:
        unique_together = ('user', 'name')


class PetPhoto(models.Model):
    photo = models.ImageField(
        upload_to='photos/',
        blank=True
    )

    tagged_pets = models.ManyToManyField(
        Pet,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    publish_date = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.IntegerField(
        default=0,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )