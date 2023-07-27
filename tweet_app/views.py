from django.shortcuts import render

# Create your views here.
def ListTweet(request):
    return render(request,'tweet_app/ListTweet.html')


def AddTweet(request):
    return render(request,'tweet_app/AddTweet.html')
