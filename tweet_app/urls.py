from . import views
from django.urls import path

app_name ="tweet_app"

urlpatterns = [
    path('',views.ListTweet,name='listtweet'),
    path('addtweet/',views.AddTweet,name='addtweet'),
    path('signup/',views.SignUpView.as_view(), name="signup"),
    path('deletetweet/<int:id>',views.Tweet_delete,name="deletetweet")
]