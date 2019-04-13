# THIS IS THE ADMIN PAGE FOR THE PROJECT & CONTROLS WHAT YOU SEE WHEN YOU GO TO siteaddress/admin

from django.contrib import admin
from .models import Product   # import the product class that we created in models.py
from django.contrib import admin   # import djangos admin class

# Register your models here.
# Note that some changes you make here may not appear on site until you restart the django server
#  using ctrl-c then   python manage.py runserver

# removes Django from top of admin page so page is not branded
# this affects all the admin pages for all the apps so is prob better put somewhere else but i dont know where to put it
admin.site.site_header = "SlimeShopping.com Site Content Management Page"


class ProductAdmin(admin.ModelAdmin):
    # found how to add ProductAdmin class below at:  https://www.youtube.com/watch?v=j-CCNJmZQ6c
    # this allows select attribs of the productss to show on the admin page instead of "Produt object (1)"
    list_display = ('shortdesc', 'sortcounter', 'image')

    def product_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(ProductAdmin, self).get_queryset(request)
        queryset = queryset.order_by('sortcounter')  # sort by sortcounter or -sortcounter.
        # (with - in front will reverse sort, lowest to highest)
        # note that this just sorts how they appear on admin page, but this line of code django code from the home.html
        # page determines how they sort on the home page:   {% for product in products.all|dictsort:"sortcounter" %}
        return queryset


# this will make our Product class show up on the website admin page
# and also makes the new optional ProductAdmin class i put on this page show up
# this must be below the ProductAdmin class or the parser won't see it
admin.site.register(Product, ProductAdmin)

