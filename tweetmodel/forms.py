from django.forms import ModelForm

from .models import TweetModel


class TweetForm(ModelForm):

    class Meta:

        model = TweetModel

        fields = ['tweet']

