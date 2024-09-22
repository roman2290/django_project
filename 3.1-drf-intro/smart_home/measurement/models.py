from django.db import models




class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Датчик')
    description = models.CharField(max_length=50, verbose_name='Описание')

    class Meta:
        ordering  = ['-id']

    def __str__(self):
            return self.name

    # class Meta: 
    #     verbose_name = 'Температура'
    #     verbose_name = 'Дата'

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement')
    temperature = models.DecimalField(max_digits = 4, decimal_places = 2, verbose_name='температура')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата')
    
    class Meta:
        ordering  = ['-created_at']
    
    def __str__(self):
            return self.temperature