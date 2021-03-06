from django.db                 import models
from django.db.models.deletion import CASCADE

from users.models              import User
from keywords.models           import Keyword
from core.models               import TimeStampModel

class Posting(TimeStampModel): 
    title         = models.CharField(max_length=100)
    sub_title     = models.CharField(max_length=200)
    content       = models.TextField()
    thumbnail     = models.URLField(max_length=1000)
    user          = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword       = models.ForeignKey(Keyword, on_delete=models.CASCADE)

    class Meta:
        db_table = 'postings'

class Like(models.Model):
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    posting      = models.ForeignKey('Posting', on_delete=models.CASCADE)

    class Meta:
        db_table = 'likes'

class Comment(TimeStampModel):
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    posting      = models.ForeignKey('Posting', on_delete=models.CASCADE, null=True)
    reply        = models.TextField()

    class Meta:
        db_table = 'comments'