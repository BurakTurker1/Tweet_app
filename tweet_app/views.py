from django.shortcuts import render
from . import models

# Create your views here.
def ListTweet(request):
    all_tweet = models.tweet.objects.all()
    context_tweet ={"tweets":all_tweet }
    return render(request,'tweet_app/ListTweet.html',context=context_tweet)


def AddTweet(request):
    return render(request,'tweet_app/AddTweet.html')
