from django.db import models
from django.conf import settings
from django.urls import reverse

class Video(models.Model):
    Video_My_Video = models.FileField(upload_to = u'video/', max_length=200)
    Video_Owned_By = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)



    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('Video_details', args=[str(self.id)])


# Create Video Comments here.


class Comment(models.Model):

    Video_Comment = models.CharField(max_length=150, null=False)
    Comment_Video = models.ForeignKey(Video, related_name='Videocommentss',null=False, on_delete=models.CASCADE)
    Video_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL   ,related_name='Videocomments', on_delete=models.CASCADE,null=True)
    Video_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Video_Comment

    def get_absolute_url(self):
        return reverse('Video_list')