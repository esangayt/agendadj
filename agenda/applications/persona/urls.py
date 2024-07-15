"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from .views import (
    ListPersons, CretePersonaAPI, RetrievePerson, DestroyPerson, UpdatePerson,
    PersonAPILista, ReunionAPILista, CreateReunionAPI, RetrieveReunionAPI, PersonPaginationLists, ReunionByPersonJob
)

app_name = 'persona_app'

urlpatterns = [
    path('api/lista-personas/', ListPersons.as_view(), name='lista_personas'),
    path('api/crear-persona/', CretePersonaAPI.as_view(), name='crear_persona'),
    path('api/ver-persona/<pk>', RetrievePerson.as_view(), name='persona-detail'),
    path('api/delete-person/<pk>', DestroyPerson.as_view(), name='delete_persona'),
    path('api/update-person/<pk>', UpdatePerson.as_view(), name='Update_persona'),
    # =======================
    path('api/list-person/', PersonAPILista.as_view(), name='list_person'),

    path('api/list-reunion/', ReunionAPILista.as_view(), name='list_reunion'),
    path('api/crear-reunion/', CreateReunionAPI.as_view(), name='crear_reunion'),
    path('api/ver-reunion/<pk>', RetrieveReunionAPI.as_view(), name='ver_reunion'),

    path('api/person-pagination/', PersonPaginationLists.as_view(), name='person_pagination'),
    path('api/cubo/reunionbyjob/', ReunionByPersonJob.as_view(), name='reunion_by_job'),

]
