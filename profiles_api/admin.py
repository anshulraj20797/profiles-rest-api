from django.contrib import admin
# from profiles_api import models
from .models import ProfileFeedItem, UserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ProfileFeedItem)
