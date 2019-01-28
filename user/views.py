from django.shortcuts import render

from django.views.generic import CreateView, TemplateView, DetailView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
# Create your views here.

from .forms import CustomUserCreationForm
from .models import CustomUser
from tweetmodel.models import TweetModel


class CreateUserView(CreateView):

    form_class = CustomUserCreationForm

    success_url = reverse_lazy('home')

    template_name = 'registration/signup.html'


class UserHomePage(DetailView):

    template_name = 'userpage.html'

    model = CustomUser

    context_object_name = "user"

    slug_field = 'username'

    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):

        context = super(UserHomePage, self).get_context_data(**kwargs)
        context['tweets'] = TweetModel.objects.all()
        return context


class CustomLogin(LoginView):

    def get_success_url(self):

        url = self.get_redirect_url()

        return url or reverse('users:userpage', args=[self.request.user.username], )


