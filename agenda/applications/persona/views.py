from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views.generic import TemplateView
from firebase_admin import auth
from rest_framework import status
from rest_framework.generics import (
ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView,
RetrieveUpdateAPIView
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Person
from .serializer import PersonasSerializer


class LoginUser(TemplateView):
    template_name = 'persona/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context


# vista que recibe un token - serializador

# Use api view
# desencriptar token
# metodo initial carga algo cuando el serialziador se carga
# class LoginView(ListAPIView):
#     serializer_class = LoginSocialSerializer

class ListPersons(ListAPIView):
    serializer_class = PersonasSerializer

    def get_queryset(self):
        return Person.objects.all()


class CretePersonaAPI(CreateAPIView):
    serializer_class = PersonasSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class RetrievePerson(RetrieveAPIView):
    serializer_class = PersonasSerializer

    def get_queryset(self):
        return Person.objects.all()


class DestroyPerson(DestroyAPIView):
    serializer_class = PersonasSerializer

    def get_queryset(self):
        return Person.objects.all()


class UpdatePerson(UpdateAPIView):
    serializer_class = PersonasSerializer

    def get_queryset(self):
        return Person.objects.all()


class RetrieveUpdatePerson(RetrieveUpdateAPIView):
    serializer_class = PersonasSerializer

    def get_queryset(self):
        return Person.objects.all()