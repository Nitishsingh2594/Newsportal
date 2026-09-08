from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class contactus(models.Model):
    Name=models.CharField(max_length=50,null=True)
    Email=models.EmailField(max_length=50,null=True)
    Mobile=models.CharField(max_length=16,null=True)
    Massage=models.TextField(null=True)
class category(models.Model):
    category_name=models.CharField(max_length=100,null=True)
    category_picture=models.ImageField(upload_to='static/category/',null=True)
    def __str__(self):
        return self.category_name
class tbl_slider(models.Model):
    picture=models.ImageField(upload_to='static/slider/',null=True)
    title=models.CharField(max_length=40,null=True)
    description=models.TextField(null=True)

class tbl_jobs(models.Model):
    title=models.CharField(max_length=50,null=True)
    title_link=models.CharField(max_length=150,null=True)
    posted_date=models.DateField(null=True)
class tbl_city(models.Model):
    city_name=models.CharField(max_length=50,null=True)
    city_picture=models.ImageField(upload_to='static/city/',null=True)
    def __str__(self):
        return self.city_name
class tbl_news(models.Model):
    headline=models.CharField(max_length=400,null=True)
    news_category=models.ForeignKey(category,on_delete=models.CASCADE)
    news_city=models.ForeignKey(tbl_city,on_delete=models.CASCADE)
    news_description=HTMLField(null=True)
    posted_date=models.DateField()
    news_picture=models.ImageField(upload_to='static/news/',null=True)
class video_news(models.Model):
    news_headline=models.CharField(max_length=400,null=True)
    news_description=HTMLField(null=True)
    video_link=models.CharField(max_length=50,null=True)
    posted_date = models.DateField(null=True)
class tbl_faq(models.Model):
    faq_qus=models.CharField(max_length=600,null=True)
    faq_ans=models.TextField(null=True)
class tbl_investor(models.Model):
    in_picture=models.ImageField(upload_to='static/investor/',null=True)
    in_name=models.CharField(max_length=100,null=True)
    in_description=HTMLField(null=True)
