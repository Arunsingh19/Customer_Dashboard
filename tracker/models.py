from django.db import models
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     email = models.EmailField(unique=True)
class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    Customer_Identifier = models.CharField(max_length=10,unique=True)
    password = models.CharField(max_length=150)

    class Meta:
        db_table = 'SuperAdmin_customers'

    def __str__(self) -> str:
        return self.Customer_Identifier
    
    USERNAME_FIELD = 'Customer_Identifier'
    REQUIRED_FIELDS = ['password']

class gfr(models.Model):
    id = models.IntegerField(primary_key=True)
    Code = models.CharField(max_length=3)
    tracker = models.CharField(max_length=150)
    Mfg = models.CharField(max_length=30)
    Device = models.CharField(max_length=15)
    SerialNo = models.CharField(max_length=15)
    SAMVer = models.CharField(max_length=150)
    hardware_Id = models.CharField(max_length=150)
    Encryption = models.CharField(max_length=20)
    SQN = models.IntegerField()
    config_ver = models.IntegerField()
    TS = models.BigIntegerField()
    PowerSource = models.CharField(max_length=20)
    last_modified =models.DateTimeField()
    version_id = models.IntegerField()
    DataRecoInfo =models.CharField(max_length=250)
    fullJSON = models.JSONField()
    fullJSON_date = models.DateTimeField()
    gereq_flag = models.IntegerField()
    SWver = models.CharField(max_length=150)

    class Meta:
        db_table = 'SuperAdmin_gfrid'
        # managed = True

class Tracker(models.Model):
    id = models.IntegerField(primary_key=True)
    customerID = models.IntegerField()
    batchId = models.IntegerField()
    mode = models.CharField(max_length=150)
    staffID_id = models.IntegerField()
    tracker = models.CharField(max_length=150)
    status = models.IntegerField()
    asset = models.CharField(max_length=150)
    application_domain = models.CharField(max_length=150)
    hardware_comments = models.CharField(max_length=500)
    software_comments = models.CharField(max_length=500)
    remarks = models.CharField(max_length=500)
    last_modified = models.DateTimeField()

    class Meta:
        db_table = 'SuperAdmin_cust_batches_trackers'

class Loadcell(models.Model):
    id = models.IntegerField(primary_key=True)
    gfrid = models.IntegerField()
    # last_modified = models.DateTimeField()
    perwght = models.CharField(max_length=10)
    avgwght = models.CharField(max_length=10)
    wghtlist = models.CharField(max_length=10)
    ts = models.BigIntegerField()
    class Meta:
        db_table = 'ldv_lcell711'

class Gps(models.Model):
    id = models.IntegerField(primary_key=True)
    gfrid = models.IntegerField()
    last_modified = models.DateTimeField()
    lat = models.CharField(max_length=50)
    lon = models.CharField(max_length=50)
    ts = models.BigIntegerField()

    class Meta:
        db_table = 'ldv_gpsl86'

class login(models.Model):
    # id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=8)
    # tracker = models.CharField(max_length=40)
    login_at = models.DateTimeField(auto_now_add=True)

class track_detail(models.Model):
    tracker = models.CharField(max_length=30)