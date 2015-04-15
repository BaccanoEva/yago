from django.db import models
from geoposition.fields import GeopositionField
from account.models import User
from feed.models import Venue


REPORTED_POST_COUNT_THRESHOLD = 3


class Post(models.Model):
    image_url = models.CharField(max_length=400)
    thumbnail_url = models.CharField(max_length=400)
    position = GeopositionField()
    user = models.ForeignKey(User, related_name='posts')
    timestamp = models.DateTimeField(auto_now_add=True)
    venue = models.ForeignKey(Venue)

    def __unicode__(self):
        return str(self.user) + "'s post at " + str(self.venue)

class ReportedPost(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post, related_name='reported_posts')


class Like(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
