from . import views
from django.urls import path

app_name ="tweet_app"

urlpatterns = [
    path('',views.ListTweet,name='listtweet'),
    path('addtweet/',views.AddTweet,name='addtweet')
]