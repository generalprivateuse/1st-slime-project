from django.db import models

# Create your models here.
# this is the models page for the PRODUCTS app
# see for dj model field types:  https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.Field


class Product(models.Model):
    image = models.ImageField(upload_to='images/')
    shortdesc = models.CharField(max_length=200)
    longdesc = models.CharField(max_length=800)
    # wayne added this one that was not in tutorial so can choose order that jobs display on home and admin pages
    # b4 adding field i backed up db and project files, added field with null=True so didn't have to deal with
    # existing records not having any value for this field, then made migrations then did a migrate
    sortcounter = models.IntegerField(null=False)

    # this allows the summary of the products to show instead of "Product object (1)"
    # but is not needed if we add "list_display = ('summary', 'image')" to the jobs\admin page
    # EXCEPT that it might allow me to see the names of objects while i'm in the python shell so i'll keep it here
    def __str__(self):
        return self.shortdesc


