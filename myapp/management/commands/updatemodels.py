from django.core.management.base import BaseCommand
import pandas as pd
from myapp.models import *




class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        df = pd.read_csv('item.csv')
        for ItemCode,ItemName,Quantity in zip(df.ItemCode, df.ItemName, df.Quantity):
            Item.create(ItemCode=ItemCode,ItemName=ItemName,Quantity=int(Quantity)).save
