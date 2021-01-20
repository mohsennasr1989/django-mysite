from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Products(models.Model):

    def __str__(self):
        return self.name

    SINGULAR_UNIT_CHOICES = (
        ('PCS', 'Pieces'),
        ('M', 'Meter'),
    )

    PLURAL_UNIT_CHOICES = (
        ('BOX', 'Box'),
        ('COIL', 'Coil'),
        ('BAR', 'Bar'),
    )

    CATEGORY_CHOICES = (
        ('PIPE_FITTING', 'Pipe & Fittings'),
        ('VALVE', 'Valves'),
        ('MANIFOLD', 'Manifolds'),
        ('UFH', 'Underfloor Heating'),
        ('TOOL', 'Tools'),
    )

    SUB_CATEGORY_CHOICES = (
        ('Box', 'BOX'),
        ('Coil', 'COIL'),
        ('Bar', 'BAR'),
    )

    code = models.CharField(max_length=20, blank=False, help_text='Product 6 digits code')
    name = models.CharField(max_length=200, blank=False, help_text='Product name')
    specification = models.CharField(max_length=300, blank=True, help_text='Product specifications')
    size = models.CharField(max_length=100, blank=True, help_text='Product size')
    singular_unit = models.CharField(max_length=10, choices=SINGULAR_UNIT_CHOICES, default='PCS', blank=False
                                     , help_text='Product singular unit')
    plural_unit = models.CharField(max_length=10, choices=PLURAL_UNIT_CHOICES, default='BOX', blank=False
                                   , help_text='Product plural unit')
    package_quantity = models.IntegerField(default=1, blank=False, help_text='Product package quantity')
    image = models.ImageField(default='product.jpg', upload_to='products_images', help_text='Product image')
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES, default='PIPE_FITTING', blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def get_absolute_url(self):
        return reverse('product:detail', kwargs={'pk': self.pk})
