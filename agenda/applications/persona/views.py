from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views.generic import TemplateView
from firebase_admin import auth
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from agendadj.agenda.applications.persona.serializer import LoginSocialSerializer


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
class LoginView(APIView):
    serializer_class = LoginSocialSerializer

    def post(self, request):
        # serializamos la data enviada por el usuario
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # token = serializer.validated_data['token']
        token = serializer.data.get('token')

        decoded_token = auth.verify_id_token(token)
        print(decoded_token)

        email = decoded_token['email']
        uid = decoded_token['name']
        avatar = decoded_token['picture', '']
        verified = decoded_token['email_verified']

        user, created = User.objects.get_or_create(

        # user = authenticate(request, token=token)
        # if user:
        #     login(request, user)
        #     return Response(
        #         {'message': 'Login exitoso'}, status=status.HTTP_200_OK
        #     )
        return Response(
            {'message': 'Token invalido'}, status=status.HTTP_400_BAD_REQUEST
        )
