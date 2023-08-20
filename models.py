from django.db import models
from tinymce.models import HTMLField
class basicinfo(models.Model):
    name=models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)
    phone= models.IntegerField()
    address=models.TextField(max_length=200)
    language=models.CharField(max_length=100)
    about=HTMLField()
    
    def __str__(self):
        return self.name
    
class workexp(models.Model):
    
    company=models.CharField(max_length=100)
    timeline=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    aboutexp=HTMLField()
    
    def __str__(self):
        return self.company
    
    
class education(models.Model):
    session=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    domain=models.CharField(max_length=100)
    institute=models.CharField(max_length=100)
    aboutit=HTMLField()
    
    def __str__(self):
        return self.course
    
    
class references(models.Model):
    reference_name=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    image=models.ImageField(upload_to="upload/")
    aboutthem=HTMLField()
    
    def __str__(self):
        return self.reference_name
    
    
    
    
class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    
    
    def __str__(self):
        return self.name
    
    
    
    
    

    
    
    

    
    
    

    
    
    
    
    
    
    
                             
    
    
    
    
    
    
    