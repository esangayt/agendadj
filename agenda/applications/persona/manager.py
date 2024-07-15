from django.db import models
#
from django.db.models import Count, F


class ReunionManager(models.Manager):
    def cantidad_reuniones_job(self):
        resultado = self.values(jobs=F('person__job')).annotate(
            cantidad=Count('*')
        )
        print(resultado.query)
        print('**************')
        print(resultado)
        return resultado
