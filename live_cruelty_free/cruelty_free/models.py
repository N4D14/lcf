from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# Create your models here.
class Company(models.Model) :
    CATEGORY_CHOICES = ((1, 'Cruelty Free'), 
                        (2, 'Tests'), 
                        (3, 'Vegan'), 
                        (4, 'PETA'), 
                        (5, 'Mall Partner'), 
                        (6, 'Vegan & PETA'), 
                        (7, 'Vegan & Mall Partner'))

    PRODUCT_CHOICES =  ((1, 'Personal Care'), 
                        (2, 'Household Care'), 
                        (3, 'Pet Care'), 
                        (4, 'Nutrition'), 
                        (5, 'Office Supplies'))

    parent = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(max_length=250)
    category = models.PositiveSmallIntegerField(choices=CATEGORY_CHOICES)
    url = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    product = models.PositiveSmallIntegerField(choices=PRODUCT_CHOICES, blank=True, null=True)
