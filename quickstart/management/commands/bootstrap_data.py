from django.core.management.base import BaseCommand
from quickstart.models import ShoeType, ShoeColor


class Command(BaseCommand):

    shoeTypes = ['sneaker', 'boot', 'sandal', 'dress', 'other']
    shoeColors = ['RD',
                  'OR',
                  'YW',
                  'GR',
                  'BU',
                  'IN',
                  'VL',
                  'WT',
                  'BL']

    def handleShoeType(self):
        for type in self.shoeTypes:
            ShoeType.objects.create(
                style=type
            )

    def handleShoeColor(self):
        for color in self.shoeColors:
            ShoeColor.objects.create(
                color_name=color
            )

    def handle(self, *args, **qwargs):
        self.handleShoeType()
        self.handleShoeColor()
