from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views.generic import TemplateView
from firebase_admin import auth
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Person
from .serializer import ListaPersonasSerializer


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
    serializer_class = ListaPersonasSerializer

    def get_queryset(self):
        return Person.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        #lista - json
        #json - lista
        serializer = ListaPersonasSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

