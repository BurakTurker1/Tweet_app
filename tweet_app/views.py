from django.shortcuts import render,redirect
from . import models
from django.urls import reverse

# Create your views here.
def ListTweet(request):
    all_tweet = models.tweet.objects.all()
    context_tweet ={"tweets":all_tweet }
    return render(request,'tweet_app/ListTweet.html',context=context_tweet)


def AddTweet(request):
    if request.POST:
       nickname = request.POST["nickname"]
       message =request.POST["message"]
       models.tweet.objects.create(nickname=nickname,message=message)
       return redirect(reverse('tweet_app:listtweet'))
    else:
        return render(request,'tweet_app/AddTweet.html')
