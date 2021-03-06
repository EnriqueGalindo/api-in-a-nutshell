from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()


class ShoeType(models.Model):
    style = models.CharField(max_length=100)

    def __str__(self):
        return self.style


class ShoeColor(models.Model):
    RED = 'RD'
    ORANGE = 'OR'
    YELLOW = 'YW'
    GREEN = 'GR'
    BLUE = 'BU'
    INDIGO = 'IN'
    VIOLET = 'VL'
    WHITE = 'WT'
    BLACK = 'BL'

    COLOR_CHOICES = [
        (RED, 'Red'),
        (ORANGE, 'Orange'),
        (YELLOW, 'Yellow'),
        (GREEN, 'Green'),
        (BLUE, 'Blue'),
        (INDIGO, 'Indigo'),
        (VIOLET, 'Violet'),
        (WHITE, 'White'),
        (BLACK, 'Black')
    ]
    color_name = models.CharField(
        max_length=2,
        choices=COLOR_CHOICES,
        default=BLACK,
    )

    def __str__(self):
        return self.color_name


class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=100)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=100)
