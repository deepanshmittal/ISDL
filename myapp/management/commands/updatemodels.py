from django.core.management.base import BaseCommand
import pandas as pd
from myapp.models import *




class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        df = pd.read_csv('data.csv')
        for Item_Code, Item_Number, BuildingId, floor, RoomFin in zip(df.Item_Code, df.ItemNumber, df.BuildingID, df.Floo, df.RoomFinal):
            model = Inventory(ItemCode=Item.objects.get(ItemCode=Item_Code), BuildingID=BuildingId, Floor=int(floor), Room=RoomFin)
            model.save()
