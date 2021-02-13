from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    #father = models.CharField(max_length=122, default="")
    #name2 = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    #phone1 = models.CharField(max_length=12)
    #MhtcetAppNo = models.CharField(max_length=12)
    #MhtcetPercentile = models.CharField(max_length=12)
    #MhtcetRank = models.CharField(max_length=12)
    #JeeAppNo = models.CharField(max_length=12)
    #JeePercentile = models.CharField(max_length=12)
    #JeeRank = models.CharField(max_length=12) 
    #Address1 = models.TextField()
    #Address2 = models.TextField()
    #CollegeName = models.CharField(max_length=122)
    #Percentage = models.CharField(max_length=12)
    #Aadhar = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    #image=models.ImageField(upload_to="images/", null=True, verbose_name="", default="")


    def __str__(self):
        return self.name

