from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Products(models.Model):
    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
        ordering = ('id', 'code', 'name', 'specification', 'size')

    def __str__(self):
        return self.name

    SINGULAR_UNIT_CHOICES = (
        ('PCS', 'عدد'),
        ('M', 'متر'),
    )

    PLURAL_UNIT_CHOICES = (
        ('BOX', 'کارتن'),
        ('COIL', 'رول'),
        ('BAR', 'شاخه'),
    )

    CATEGORY_CHOICES = (
        ('PIPE_FITTING', 'لوله و اتصالات'),
        ('VALVE', 'شیرآلات'),
        ('MANIFOLD', 'کلتور'),
        ('UFH', 'گرمایش از کف'),
        ('TOOL', 'ابزار'),
    )

    SUB_CATEGORY_CHOICES = (
        ('Box', 'BOX'),
        ('Coil', 'COIL'),
        ('Bar', 'BAR'),
    )

    code = models.CharField(verbose_name="کد محصول", max_length=20, blank=False, help_text='Product 6 digits code')
    name = models.CharField(verbose_name="نام محصول", max_length=200, blank=False, help_text='Product name')
    specification = models.CharField(verbose_name="مشخصات", max_length=300, blank=True, help_text='Product '
                                                                                                  'specifications')
    size = models.CharField(verbose_name="سایز", max_length=100, blank=True, help_text='Product size')
    singular_unit = models.CharField(verbose_name="واحد", max_length=10, choices=SINGULAR_UNIT_CHOICES, default='PCS',
                                     blank=False, help_text='Product singular unit')
    plural_unit = models.CharField(verbose_name="واحد بسته", max_length=10, choices=PLURAL_UNIT_CHOICES, default='BOX',
                                   blank=False, help_text='Product plural unit')
    package_quantity = models.IntegerField(verbose_name="تعداد در بسته", default=1, blank=False,
                                           help_text='Product package quantity')
    image = models.ImageField(verbose_name="تصویر", default='product.jpg', upload_to='products_images',
                              help_text='Product image')
    category = models.CharField(verbose_name="دسته", max_length=200, choices=CATEGORY_CHOICES, default='PIPE_FITTING',
                                blank=False)
    price = models.FloatField(verbose_name="قیمت", default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def get_absolute_url(self):
        return reverse('product:detail', kwargs={'pk': self.pk})