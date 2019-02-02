from django.core.exceptions import PermissionDenied
from django.views.generic import CreateView, DeleteView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from .models import TweetModel
from .forms import TweetForm
# Create your views here.


class CreateTweet(LoginRequiredMixin, CreateView):

    #form_class = TweetForm

    model = TweetModel

    template_name = 'tweet.html'

    fields = ('tweet',)

    def get_success_url(self):

        return reverse('users:userpage', args=[self.request.user.username], )

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteTweet(LoginRequiredMixin, DeleteView):

    model = TweetModel

    template_name = 'delete_tweet.html'

    login_url = 'users:login'

    def get_success_url(self):

        return reverse('users:userpage', args=[self.request.user.username], )

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.user != self.request.user:
            raise PermissionDenied

        return super().delete(request, *args, **kwargs)


class ViewTweet(DetailView):

    model = TweetModel

    context_object_name = 'tweet'


class ViewTweets(ListView):

    model = TweetModel

    context_object_name = 'tweets'

