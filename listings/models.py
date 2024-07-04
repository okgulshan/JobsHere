from django.db import models

# Create your models here.
class Listing(models.Model):
    companyname = models.CharField(max_length=200)
    jobtype = models.CharField(max_length=200)
    role = models.TextField()
    jobdescription = models.TextField()
    responsibilities = models.TextField(blank=True)
    qualifications = models.TextField()
    gainsandbenefits = models.TextField()
    additionalinformation = models.TextField()
    banner = models.ImageField(null=True,upload_to="listings/")
    location = models.CharField(max_length=250,null=True)

class JobListing(models.Model):
    companyname = models.CharField(max_length=200)
    jobtype = models.CharField(max_length=200)
    role = models.TextField()
    jobdescription = models.TextField()
    responsibilities = models.TextField(blank=True)
    qualifications = models.TextField()
    gainsandbenefits = models.TextField()
    additionalinformation = models.TextField()
    banner = models.ImageField(null=True,upload_to="static/images/")
    location = models.CharField(max_length=250,null=True)

from django.db import models

# Create your models here.
class contactUs(models.Model):
    yourname=models.CharField(max_length=50) 
    email=models.EmailField()
    message=models.TextField()


class reportIssue(models.Model):
    reportedby=models.CharField(max_length=50) 
    Description=models.TextField()

class JobApplication(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    companies = models.TextField()
    ques1 = models.TextField()
    ques2 = models.TextField()
    ques3 = models.TextField()
    resume = models.FileField(upload_to="banner/images/")