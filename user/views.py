from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from user.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from user.models import User


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    form_class = UserLoginForm


class UserRegistrationView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('user:login')
    success_message = 'Вы успешно зарегестрированы!'


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'user/profile.html'

    def get_success_url(self):
        return reverse_lazy('user:profile', args=(self.object.id,))
