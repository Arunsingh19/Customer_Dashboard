from rest_framework.serializers import ModelSerializer
from .models import Customer, Gps, login, track_detail
from tracker.models import Loadcell, Tracker, gfr

class GfrSerializer(ModelSerializer):
    class Meta:
        model = gfr
        fields = '__all__'
        # fields = ['id','Code','tracker','Mfg']

class TrackerSerializer(ModelSerializer):
    class Meta:
        model = Tracker
        # fields = '__all__'
        fields = ['tracker']
        # exclude = ['id']

class LoadcellSerializer(ModelSerializer):
    class Meta:
        model = Loadcell
        fields = ['ts','perwegt']

class GPSSerializers(ModelSerializer):
    class Meta:
        model = Gps
        fields = ['lat','lon','ts']

class LoginSerializers(ModelSerializer):
    class Meta:
        model = login
        fields = ['username','password','tracker']
    
class CustomerSerializers(ModelSerializer):
    class Meta:
        model = Customer
        fields = ['Customer_Identifier','password']

class trackerdetailserializers(ModelSerializer):
    class Meta:
        model = track_detail
        fields = '__all__'

class llserializer(ModelSerializer):
    class Meta:
        model = Loadcell
        fields = ['perwght','ts']

class glserializer(ModelSerializer):
    class Meta:
        model = Gps
        fields = ['lat','lon','ts']


