from django.shortcuts import render
from django.views.generic import TemplateView


class LoginUser(TemplateView):
    template_name = 'persona/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context
