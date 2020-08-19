from django.db import models
from django.utils import timezone


class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length = 200)

    def __str__(self):
        return self.cat_name

class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    topic_name = models.CharField(max_length=200)
    topic_category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.topic_name

class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_title = models.CharField(max_length=200)
    book_topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    book_isbn = models.IntegerField()
    book_no_of_page = models.IntegerField()
    book_author = models.CharField(max_length=200)
    book_desc = models.TextField()
    QUALITY = (("New Like","New Like"),("Good Condition","Good Condition"),("Too old","Too old"))
    book_quality = models.CharField(max_length=200,choices=QUALITY)
    book_price = models.IntegerField()
    book_doc = models.DateTimeField(default=timezone.now)
    book_status = models.IntegerField(default=0)
    book_cover = models.ImageField(upload_to='books/',default="default.jpg",blank=True)
    book_contact = models.IntegerField(default = 0000000000)
    book_address = models.CharField(max_length = 200,default = "Not available")

    def __str__(self):
        return self.book_title