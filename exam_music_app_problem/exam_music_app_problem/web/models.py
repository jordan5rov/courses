from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from exam_music_app_problem.web.validators import only_letters_numbers_underscore_validator


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 15
    USERNAME_MIN_LENGTH = 2

    AGE_MIN_VALUE = 0
    AGE_DEFAULT_VALUE = 0

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(USERNAME_MIN_LENGTH),
            only_letters_numbers_underscore_validator,
        ),
    )
    email = models.EmailField()
    age = models.IntegerField(
        null=True,
        blank=True,
        default=AGE_DEFAULT_VALUE,
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        ),
    )


class Album(models.Model):
    NAME_MAX_LENGTH = 30

    ARTIST_MAX_LENGTH = 30

    POP_MUSIC = "Pop Music"
    JAZZ_MUSIC = "Jazz Music"
    R_AND_B_MUSIC = "R&B Music"
    ROCK_MUSIC = "Rock Music"
    COUNTRY_MUSIC = "Country Music"
    DANCE_MUSIC = "Dance Music"
    HIP_HOP_MUSIC = "Hip Hop Music"
    OTHER = "Other"

    GENRES = [(x, x) for x in (POP_MUSIC, JAZZ_MUSIC, R_AND_B_MUSIC, ROCK_MUSIC, COUNTRY_MUSIC, DANCE_MUSIC,
                               HIP_HOP_MUSIC, OTHER)]
    GENRE_MAX_LENGTH = 30

    PRICE_MIN_VALUE = 0

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
    )
    artist = models.CharField(
        max_length=ARTIST_MAX_LENGTH,
    )
    genre = models.CharField(
        max_length=GENRE_MAX_LENGTH,
        choices=GENRES,

    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField()
    price = models.FloatField(
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        ),
    )
