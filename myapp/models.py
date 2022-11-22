from django.contrib.auth.models import User
from django.db import models

# Create your models here.

"""
create table Item (
  Item_Code varchar(255), 
  Name varchar(255), 
  Latest_Price int, 
  QuantityInInventory int, 
  PRIMARY KEY (Item_Code)
);
create table Inventory(
  buildingID varchar(5), 
  flor varchar(2), 
  room varchar(4), 
  Item_Code varchar(8), 
  num int(10),
  status varchar(255),inuse,buffer
  primary key(
    buildingID, flor, room, Item_Code, 
    num
  ), 
  foreign key(Item_Code) references Item(Item_Code)
);
create table Purchase(
  Reg_no int(10) AUTO_INCREMENT, 
  Status varchar(255), pending, incomplete, Completed
  primary key(Reg_no)
);
create table ItemList(
  Reg_no int (10) AUTO_INCREMENT, 
  Item_Code varchar(8), 
  quantity int(5),
  foreign key(Reg_no) references Purchase (Reg_no), 
  foreign key(Item_Code) references Item(Item_Code)
);
create table Quotation(
  Reg_No int(10), 
  quotee varchar(255), 
  amount int(10), 
  stat varchar(255), 
  foreign key(Reg_No) references purchase(Reg_No)
);
"""


class Profile(models.Model):
    FirstName = models.CharField(max_length=32)
    LastName = models.CharField(max_length=32)
    Role = models.CharField(max_length=32, choices=[("IM", "Inventory Manager"), ("PO", "Purchase Officer"),
                                                    ("MGIM", "Main Gate Inventory Manager")])
    Owner = models.OneToOneField(User, on_delete=models.CASCADE)


class Item(models.Model):
    Name = models.CharField(max_length=128)
    ItemCode = models.CharField(max_length=16, primary_key=True)
    Quantity = models.PositiveIntegerField(default=0)


class Inventory(models.Model):
    BuildingID = models.CharField(max_length=8)
    Floor = models.PositiveIntegerField()
    Room = models.CharField(max_length=8)
    ItemCode = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    ItemNumber = models.BigAutoField(primary_key=True)


# Bill corresponding to items in itemlist
class Bill(models.Model):
    RegNo = models.BigAutoField(primary_key=True)
    Date = models.DateField(auto_now_add=True)


class ItemList(models.Model):
    Bill = models.ForeignKey(Bill, on_delete=models.DO_NOTHING)
    ItemCode = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    Quantity = models.PositiveIntegerField()


class Quotation(models.Model):
    Bill = models.ForeignKey(Bill, on_delete=models.DO_NOTHING)
    QuotationLink = models.URLField()
    Quotee = models.CharField(max_length=64)
    Amount = models.PositiveIntegerField()
    # Pending, Approved, Declined, Ordered
    Status = models.CharField(max_length=16, default='Pending',
                              choices=[("Pending", "Pending"), ("Declined", "Declined"),
                                       ("Approved", "Approved")])


class Purchase(models.Model):
    Bill = models.OneToOneField(
        Bill, primary_key=True, on_delete=models.DO_NOTHING)
    # Pending, Complete
    Quotation = models.ForeignKey(Quotation, on_delete=models.DO_NOTHING)
    Status = models.CharField(max_length=16, default='Pending',
                              choices=[("Pending", "Pending"), ("Complete", "Complete")])
    DateCreated = models.DateField(auto_now_add=True)


class MainGateEntry(models.Model):
    RegNo = models.ForeignKey(ItemList, on_delete=models.DO_NOTHING)
    ItemCode = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    Quantity = models.PositiveIntegerField()
