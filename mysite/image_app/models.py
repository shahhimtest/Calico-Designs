from django.db import models

# Create your models here.
class Cats(models.Model): 
    name = models.CharField(max_length=50)
    petname = models.CharField(max_length=50) 
    cat_img = models.ImageField(upload_to='image')
    #cat_img2 = models.ImageField(upload_to='image', blank = True)
    #cat_img3 = models.ImageField(upload_to='image', blank = True)
    cat_drawing = models.ImageField(upload_to='drawings', default = 'no_image.jpg')
    addr1 = models.CharField(max_length=50)  
    addr2 = models.CharField(max_length=50) 
    itn = models.CharField(max_length=50, blank = True)
    city = models.CharField(max_length=50) 
    state = models.CharField(max_length=50) 
    postcode = models.CharField(max_length=50) 
    contact = models.CharField(max_length=50) 
    venmo = models.CharField(max_length=50)
    show = models.BooleanField(default=False)

