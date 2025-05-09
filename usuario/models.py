from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from usuario.managers import CustomUserManager
from uploader.models import Image
from core.models.enterprise import Enterprise

class Usuario(AbstractUser):
    username = None
    email = models.EmailField(_("e-mail address"), unique=True)
    registration = models.CharField(max_length=100, unique=True, default=None)
    perfil = models.ForeignKey(Image, on_delete=models.CASCADE, default=None, null=True, blank=True, related_name='+')
    enterprise = models.ForeignKey(Enterprise, on_delete=models.PROTECT, related_name='usuarios', default=None)

    USERNAME_FIELD = "registration"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.registration

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["-date_joined"]
