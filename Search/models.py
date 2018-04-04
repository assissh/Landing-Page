from Location_Category.models import Location_Category
from Location.models import Location
from django.conf import settings
from location_subcategory.models import LocationSubCategory

from django.urls import reverse

# Create your Searchs here.


from django.db import models

class Search(models.Model):
 Search_CATEGORY= models.ForeignKey(Location_Category,related_name='Searchcategory', on_delete=models.CASCADE,null=True)
 Search_City = models.CharField(max_length=100)
 Search_Key_Word = models.CharField(max_length=200)
 Search_Location_List= models.ForeignKey(Location,related_name='Searchlocationlist', on_delete=models.CASCADE,null=True)
 Search_Range = models.IntegerField()
 Search_Sub_Category= models.ForeignKey(LocationSubCategory,related_name='SearchSubCategory', on_delete=models.CASCADE,null=True)
 Search_Creator = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='Search',on_delete=models.CASCADE,null=True)
 Search_Created_Date = models.DateTimeField(auto_now_add=True)
 Search_Modified_Date = models.DateTimeField(auto_now_add=True)




 def __str__(self):
        return self.Search_City

 def get_absolute_url(self):
        return reverse('search_details', args=[str(self.id)])


# Create Searchs Comments here.


class Comment(models.Model):

    Search_Comment = models.CharField(max_length=150, null=False)
    Comment_Search = models.ForeignKey(Search, null=False,related_name='commentSearch', on_delete=models.CASCADE)
    Search_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='SearchcommentSearch', on_delete=models.CASCADE)

    # Search_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Search_Comment_Author

    def get_absolute_url(self):
        return reverse('search_list')
