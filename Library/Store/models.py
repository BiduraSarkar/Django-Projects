from django.db import models

# Create your models here.
#note that models are classes which inherit property of Model Class
class Book(models.Model):

    def __str__(self):
        return "Name = " + self.book_name + " Author = "+ self.author + " Publisher = " + self.publisher + " Genre = " + self.genre + " Edition = " + str(self.edition) + "\n"
    
    book_name = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    publisher = models.CharField(max_length = 255)
    edition = models.IntegerField(default = 1)
    genre = models.CharField(max_length = 255)
    image = models.CharField(max_length = 255,default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNHV0HnZFjnPVeDJnh_jxfSaaxOJaazyc6Kw&s")
