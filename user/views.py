from django.shortcuts import render

from django.views.generic import CreateView, TemplateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

from .forms import CustomUserCreationForm
from .models import CustomUser

class CreateUserView(CreateView):

    form_class = CustomUserCreationForm

    success_url = reverse_lazy('home')

    template_name = 'signup.html'


class UserHomePage(DetailView):

    template_name = 'userpage.html'

    model = CustomUser

    context_object_name = "user"

    slug_field = 'username'

    slug_url_kwarg = 'username'


