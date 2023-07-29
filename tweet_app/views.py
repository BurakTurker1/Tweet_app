from django.shortcuts import render,redirect
from . import models
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView 

# Create your views here.
def ListTweet(request):
    all_tweet = models.tweet.objects.all()
    context_tweet ={"tweets":all_tweet }
    return render(request,'tweet_app/ListTweet.html',context=context_tweet)

@login_required(login_url="/login")
def AddTweet(request):
    if request.POST:
       message =request.POST["message"]
       models.tweet.objects.create(username=request.user,message=message)
       return redirect(reverse('tweet_app:listtweet'))
    else:
        return render(request,'tweet_app/AddTweet.html')
    

@login_required
def Tweet_delete(request,id):
    tweet=models.tweet.objects.get(pk=id)
    if request.user == tweet.username:
        models.tweet.objects.filter(id=id).delete()
        return redirect('tweet_app:listtweet')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"