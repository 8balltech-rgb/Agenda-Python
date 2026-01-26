from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)

    USER_TYPE_CHOICES = (
        ("player", "Jugador"),
        ("team", "Equipo"),
    )

    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    # jugador
    full_name = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    # equipo
    team_name = models.CharField(max_length=150, blank=True)
    responsible_person = models.CharField(max_length=150, blank=True)
    players_count = models.IntegerField(null=True, blank=True)
