#
from model_utils.models import TimeStampedModel
#
from django.db import models

from agendadj.agenda.applications.persona.manager import ReunionManager


class Hobby(TimeStampedModel):
    """ Modelo para registrar hobbies de una persona """

    name = models.CharField(
        'Nombre',
        max_length=50,
    )

    class Meta:
        verbose_name = 'Hobby'
        verbose_name_plural = 'Hobbies'

    def __str__(self):
        return self.name


class Person(TimeStampedModel):
    """  Modelo para registrar personas de una agenda  """

    full_name = models.CharField(
        'Nombres',
        max_length=50,
    )
    job = models.CharField(
        'Trabajo',
        max_length=30,
        blank=True
    )
    email = models.EmailField(
        blank=True,
        null=True
    )
    phone = models.CharField(
        'telefono',
        max_length=15,
        blank=True,
    )
    hobbies = models.ManyToManyField(Hobby)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return self.full_name


class Reunion(TimeStampedModel):
    """ Modelo para registrar reuniones de una persona """

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='reuniones'
    )
    fecha = models.DateField()
    hora = models.TimeField()
    asunto = models.CharField(
        'Asunto de Reunión',
        max_length=100
    )

    objects = ReunionManager()

    class Meta:
        verbose_name = 'Reunion'
        verbose_name_plural = 'Reuniones'

    def __str__(self):
        return self.asunto
