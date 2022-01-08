
from django.db import models
from django.db.models.fields import CharField
import os
from django.utils.timezone import now
from django.contrib.auth.models import User

############# Vindy Notice Models################
class Notice(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    link = models.URLField(max_length=200)
    created = models.DateTimeField(default=now, editable=False)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title


########## Vindy Team Models#######################        
class Team_Type(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Team_member(models.Model):
    category = models.ForeignKey(Team_Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    designation = models.CharField(max_length=50)
    link = models.URLField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='hwc')

    def __str__(self):
        return self.designation

############ Vindy Feeds ######################
class Feed_Type(models.Model):
    category = models.CharField(max_length=50, help_text="Please define a single worded category")
    def __str__(self):
        return self.category

class Feed(models.Model):
    #author = models.ForeignKey(User) will introduce this feature 
    # after introduction of login functionality
    category = models.ForeignKey(Feed_Type, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    intro = models.TextField(max_length=200, blank = True, help_text="This will be visible on feed card")
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'post', blank =True)
    timing = models.TextField(max_length=100, blank = True, help_text="leave blank if not event feed")
    location = models.TextField(max_length=100, blank = True, help_text="leave blank if not event feed")
    contact = models.TextField(max_length=100, default=0, help_text="leave blank if not event feed")
    link = models.URLField(blank=True,help_text="leave blank if not event feed")

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title[0:20]
    

    




    






