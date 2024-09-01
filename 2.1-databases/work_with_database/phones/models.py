from django.db import models
import uuid

class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length= 65, verbose_name='Модель телефона')
    image = models.URLField(default=None)
    price = models.IntegerField(default=None)
    release_date = models.DateField(default=None)
    lte_exists = models.BooleanField(default=None)
    slug  = models.SlugField(default=None)
    
