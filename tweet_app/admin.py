from django.contrib import admin
from tweet_app.models import tweet
# Register your models here.
class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nicname Group', {'fields':["nickname"]}),
        ('Message Group', {'fields':["message"]}),
    ]
    
admin.site.register(tweet,TweetAdmin)
