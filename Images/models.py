from django.db import models
from django.conf import settings
from django.urls import reverse

class Image(models.Model):
    Image_My_Image = models.ImageField()
    Image_Owned_By = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)



    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('Image_details', args=[str(self.id)])


# Create Image Comments here.


class Comment(models.Model):

    Image_Comment = models.CharField(max_length=150, null=False)
    Comment_Image = models.ForeignKey(Image, related_name='imagecommentss',null=False, on_delete=models.CASCADE)
    Image_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL   ,related_name='imagecomments', on_delete=models.CASCADE,null=True)
    Image_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_Comment

    def get_absolute_url(self):
        return reverse('image_list')
