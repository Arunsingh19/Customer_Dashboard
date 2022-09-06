from inspect import Parameter
from django.contrib import auth
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Customer, Gps, login, track_detail
# from django import forms

from tracker.models import Loadcell, Tracker, gfr
# from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer

# class UserCreateSerializer(BaseUserCreateSerializer):
#     class Meta(BaseUserCreateSerializer.Meta):
#         fields = ['id','username','password','email','first_name','last_name']
        
# class UserSerializer(BaseUserSerializer):
#     class Meta(BaseUserSerializer.Meta):
#         fields = ['id','username','email','first_name','last_name']

class GfrSerializer(ModelSerializer):
    class Meta:
        model = gfr
        fields = '__all__'
        # fields = ['id','Code','tracker','Mfg']

class TrackerSerializer(ModelSerializer):
    # name = serializers.CharField(max_length=60, help_text="Your help text here....")
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
        fields = ['lat','lan','ts']

class LoginSerializers(ModelSerializer):
    # username = serializers.CharField(max_length=30)
    # password = serializers.CharField(max_length=10)
    class Meta:
    #     # username = serializers.CharField(max_length=30)
    #     # password = serializers.CharField(max_length=10)
        model = login
        fields = ['username','password','tracker']
    
class CustomerSerializers(ModelSerializer):
    # username = serializers.Field(source='Customer_Identifier')
    class Meta:
        model = Customer
        fields = ['Customer_Identifier','password']

class trackerdetailserializers(ModelSerializer):
    class Meta:
        model = track_detail
        fields = '__all__'



# class login_serializer(forms.Form):
#     username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
#     password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}))
#     fields = ['username', 'password']

# class TrackerSerializer(ModelSerializer):
#     # name = serializers.CharField(max_length=60, help_text="Your help text here....")
#     username = serializers.CharField(max_length=30)
#     password = serializers.CharField(max_length=8)
#     def validate(self, attrs):
#         username = attrs.get('username','')
#         password = attrs.get('password','')

        
#         user = auth.authenticate(username=username,password=password)
#         if not user.is_active:
#             raise AuthenticationFailed("Account disable")
#         if not user:
#             raise AuthenticationFailed("invalid")
#         return super().validate(attrs)


