from django.core.management.base import BaseCommand
import pandas as pd
from myapp.models import *




class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        pass
