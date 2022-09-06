# from urllib import request
# from django.shortcuts import render
# from rest_framework import permissions
# from rest_framework.viewsets import ModelViewSet
from urllib import response
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import HttpResponseRedirect,HttpResponsePermanentRedirect
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.serializers import TokenVerifySerializer
from rest_framework.decorators import api_view,permission_classes,authentication_classes,action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import redirect,render
from django.contrib.auth.views import UserModel
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse,HttpResponse
from .forms import LoginForm
import requests,datetime
from datetime import datetime as dt

from tracker.models import Gps, Loadcell, Tracker, gfr, Customer, login
from tracker.serializers import CustomerSerializers, GfrSerializer,LoadcellSerializer, LoginSerializers,TrackerSerializer, trackerdetailserializers

# @api_view(['GET'])
# def getRoute(request):
#     routes = [
#         '/login',
#         '/gfr',
#         '/tracker'
#         # '/data'
#     ]
#     return Response(routes)

# @api_view(['GET'])
# def getData(request):
#     routes = [
#         '/gfr',
#         '/tracker'
#     ]
#     return Response(routes)

# class GfrView(ModelViewSet):
#     http_method_names = ['get']
#     permission_classes =[permissions.IsAuthenticated]
#     queryset = gfr.objects.all()
#     serializer_class = GfrSerializer
    # def get_queryset(self):
    #     Gfr = gfr.objects.get(id=request.user.id)
    #     serializer = GfrSerializer(Gfr)
    #     return Response(serializer.data)
        

# @api_view(['get'])
# @permission_classes([IsAuthenticated])
# def gfr_detail(request):
#     Gfr = gfr.objects.get(id=request.user.id)
#     serializer = GfrSerializer(Gfr)
#     return Response(serializer.data)

# @api_view(['get'])
# @permission_classes([IsAuthenticated])
# def tracker_detail(request):
#     tracker = Tracker.objects.filter(customerID=request.user.id)
#     # tracker = Tracker.objects.all().filter(customerID=request.user.id)
#     serializer = TrackerSerializer(tracker,many=True)
#     return Response(serializer.data)

# valid_code
# @api_view(['GET','POST'])
# def Tracker_Detail(request):
#     global user
#     user = 0
#     if request.method == 'GET':
#         r=request.GET.get('id')
#         res = str(r)
#         cus = Customer.objects.get(id=res)
#         serializer = CustomerSerializers(cus)
#         return Response(serializer.data)
#     # myuser = User.objects.create_user(Customer.Customer_Identifier,Customer.Email,Customer.password)
#     if request.method =='POST':
#         serializer = LoginSerializers(data=request.data)
#         if serializer.is_valid():
#             customer=Customer.objects.filter(Customer_Identifier=serializer.data['Customer_Identifier'],password=serializer.data['password']).exists()
#         # return Response(customer)
#         # user = Customer.objects.get(Customer_Identifier=serializer.data['username']).id
#             # if customer is True:
#                 # user = Customer.objects.first()
#                 # refresh = RefreshToken.for_user(user)
#                 # raw_token = str(refresh.access_token)
#                 # jwt_a = JWTAuthentication()
#                 # validated_token = jwt_a.get_validated_token(raw_token)
#                 # return Response(validated_token.)
#                 # # repr(validated_token)
#                 # # print(validated_token["user_id"])
#             if customer is True:
#                 return redirect("http://127.0.0.1:8000/tracker/")
#                 # response = Response()
#                 # response = redirect("http://127.0.0.1:8000/tracker/")
#                 # token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYwNzI3MTc4LCJqdGkiOiI2MDI4NjM0OTk3ZDI0MDQ1YjRlZDcxYjM3ZDQxM2Y4MyIsInVzZXJfaWQiOjF9.FXZ_9KQkK_MZakvfmciZujINrQqTjrhVIZmQn6jhcoU'
#                 # response['JWT'] = token
#                 # return(response)
#                 return Response("valid")
#                 # user = Customer.objects.get(Customer_Identifier=serializer.data['username']).id
#                 # return redirect('/tracker/')
#                 # customer = Customer.objects.first()
#                 # refresh = RefreshToken.for_user(customer)
#                 # access = str(refresh.access_token)
#                 # response.data = {
#                     # 'access' : access,
#                     # 'url' : "http://127.0.0.1:8000/tracker"
#                 # }
#                 # token = request.COOKIES.get('access')
#                 # request.META['HTTP_AUTHORIZATION']=f'JWT {token}'
#                 # return response
#                     # refresh = self.get_token(self.user)

#                 # response = Response()
#                 # user = Customer.objects.get(Customer_Identifier=serializer.data['Customer_Identifier']).id
#                 # response.data = {
#                 # 'id' : user,
#                 # 'refresh': str(refresh),
#                 # 'access': str(refresh.access_token),
#                 # 'tracker' : "http://127.0.0.1:8000/tracker"
#                 # }
#                 # redirect("http://127.0.0.1:8000/tracker/")
#                 # return Response(headers={'Accept': 'application/json','Content-Type': 'application/json',"Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYwNzI3MTc4LCJqdGkiOiI2MDI4NjM0OTk3ZDI0MDQ1YjRlZDcxYjM3ZDQxM2Y4MyIsInVzZXJfaWQiOjF9.FXZ_9KQkK_MZakvfmciZujINrQqTjrhVIZmQn6jhcoU"})
#                 # return Response("http://127.0.0.1:8000/tracker/", headers={'Accept': 'application/json','Content-Type': 'application/json',"Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYwNzI3MTc4LCJqdGkiOiI2MDI4NjM0OTk3ZDI0MDQ1YjRlZDcxYjM3ZDQxM2Y4MyIsInVzZXJfaWQiOjF9.FXZ_9KQkK_MZakvfmciZujINrQqTjrhVIZmQn6jhcoU"})
#                 # data = {'token': access}
#                 # valid_data = TokenVerifySerializer().validate(data)
#                 # return Response(valid_data)
#                 # return Response(jwt_token)
#                 # res = requests.get("http://127.0.0.1:8000/tracker/", headers={'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYwNzI3MTc4LCJqdGkiOiI2MDI4NjM0OTk3ZDI0MDQ1YjRlZDcxYjM3ZDQxM2Y4MyIsInVzZXJfaWQiOjF9.FXZ_9KQkK_MZakvfmciZujINrQqTjrhVIZmQn6jhcoU'})
#                 # return Response(res)
#                 # return response
#                 # redirect('http://127.0.0.1:8000/tracker/')
#                 # url = 'http://127.0.0.1:8000/tracker/'
#                 # headers = {'Accept': 'application/json',
#                 #             'Content-Type': 'application/json',
#                 #             'Authorization': f'JWT {access}'}
#                 # headers = {'Authorization' : 'JWT' f"{access}"}
#                 # jwt_token =  'JWT'+" "+ str(refresh.access_token)
#                 # headers = {'Authorization': jwt_token}
#                 # r = requests.get(url='http://127.0.0.1:8000/tracker/', headers=headers).json()
#                 # print(r.text)
#                 # return Response("http://127.0.0.1:8000/tracker")
#                 # return redirect("http://127.0.0.1:8000/tracker/",r)
#                 # response['WWW-Authenticate'] = jwt_token
#                 # redirect("http://127.0.0.1:8000/tracker/")
#                 # head = {}
#                 # head['Cache-Control'] = 'no-cache'
#                 # head['Content-Type'] = 'application/json'
#                 # head['xyzId'] = '3223'
#                 # head['abcData'] = 'ABC-123'
#                 # x = request.post(url='http://127.0.0.1:8000/tracker/',headers = head)
#                 # res = requests.get(url="http://127.0.0.1:8000/tracker/",headers=headers).json()
#                 # return Response(res)
#                 # return Response(headers)
#                 # return Response("http://127.0.0.1:8000/tracker/",)
#                 # # r = requests.get(url)
#                 # return HttpResponseRedirect(url)
#                 # return response
#                 # # else:
#                 # #     return Response("user not found")
#             else:
#                 return Response("invalid")

# @api_view(['get','post'])
# # @permission_classes([IsAuthenticated])
# def tracker_detail(request):
#     if request.method == 'GET':
#         tracker = Tracker.objects.all()
#         serializer = TrackerSerializer(tracker,many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         data = gfr.objects.get(tracker=request.data).id
#         gfr1 = gfr.objects.filter(id=data)
#         serializer = GfrSerializer(gfr1,many=True)
#         return Response(serializer.data)


# main
# @api_view(['get','post'])
# @permission_classes([IsAuthenticated])
# # @authentication_classes([JWTAuthentication])
# def tracker_detail(request):
# class TrackerView(APIView):
#     global user
#     # renderer_classes = [TemplateHTMLRenderer]
#     # permission_classes = [IsAuthenticated]
#     def get(self,request):
#         # if request.method == 'GET':
#         tracker = Tracker.objects.filter(customerID=user)
#         serializer = TrackerSerializer(tracker,many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         if gfr.objects.filter(tracker=request.data).exists():
#             # if Loadcell.objects.filter(gfrid=gfr.id):
#             data = gfr.objects.get(tracker=request.data).id
#             loadcell = Loadcell.objects.filter(gfrid=data)
#             serializer= LoadcellSerializer(loadcell,many=True)
#             return Response({'tracker': serializer.data})
#             # else:
#             #     return Response("gfrid not connected to loadcell")
#         else: 
#             return Response("this tracker not in gfr",status=status.HTTP_404_NOT_FOUND)
        # return render(request,'tracker/tracker.html',{
        #     'tracker' : serializer['tracker']
        # })
        # return render(request, 'index.html', {'name':'Customer', 'result':list(serializer.data)})
        # return Response(serializer.data)
    # elif request.method == 'POST':
    #     if gfr.objects.filter(tracker=request.data).exists():
    #         # if Loadcell.objects.filter(gfrid=gfr.id):
    #         data = gfr.objects.get(tracker=request.data).id
    #         loadcell = Loadcell.objects.filter(gfrid=data)
    #         serializer= LoadcellSerializer(loadcell,many=True)
    #         return Response(serializer.data)
    #         # else:
    #         #     return Response("gfrid not connected to loadcell")
    #     else: 
    #         return Response("this tracker not in gfr",status=status.HTTP_404_NOT_FOUND)
            # return Response(serializer.data)

# @api_view(['get','post'])
# # @permission_classes([IsAuthenticated])
# def tracker_detail(request):
#     if request.method == 'GET':
#         tracker = Tracker.objects.all()
#         serializer = TrackerSerializer(tracker,many=True)
#         return Response(serializer.data,template_name='index.html')
#     elif request.method == 'POST':
#         if gfr.objects.filter(tracker=request.data).exists():
#             # if Loadcell.objects.filter(gfrid=gfr.id):
#             data = gfr.objects.get(tracker=request.data).id
#             loadcell = Loadcell.objects.filter(gfrid=data)
#             serializer= LoadcellSerializer(loadcell,many=True)
#             return Response(serializer.data)
#             # else:
#             #     return Response("gfrid not connected to loadcell")
#         else: 
#             return Response("this tracker not in gfr",status=status.HTTP_404_NOT_FOUND)
#             # return Response(serializer.data)

# class TrackerView(APIView):
#     global user
#     # renderer_classes = [TemplateHTMLRenderer]
#     # permission_classes = [IsAuthenticated]
#     def get(self,request):
#         return Response(user)
        # if request.method == 'GET':
        # tracker = Tracker.objects.filter(customerID=user)
        # return Response(tracker)
        # serializer = TrackerSerializer(tracker,many=True)
        # if gfr.objects.filter(tracker=request.data).exists():
        #     # if Loadcell.objects.filter(gfrid=gfr.id):
        #     data = gfr.objects.get(tracker=request.data).id
        #     loadcell = Loadcell.objects.filter(gfrid=data)
        #     serializer= LoadcellSerializer(loadcell,many=True)
        #     return Response({'tracker': serializer.data})
        # else:
        #     return Response("gfrid not connected to loadcell")

# # #main
# @api_view(['GET','POST'])
# def Tracker_Detail(request):
#     global user
#     user = 0
#     if request.method == 'GET':
#         r=request.GET.get('id')
#         res = str(r)
#         cus = Customer.objects.get(Customer_Identifier=res)
#         serializer = CustomerSerializers(cus)
#         return Response(serializer.data)

#     if request.method =='POST':
#         serializer = LoginSerializers(data=request.data)
#         if serializer.is_valid():
#             user = Customer.objects.get(Customer_Identifier=serializer.data['Customer_Identifier']).id
#             customer=Customer.objects.filter(Customer_Identifier=serializer.data['Customer_Identifier'],password=serializer.data['password']).exists()
#             if customer is True:
#                 return redirect("http://127.0.0.1:8000/tracker/")
#             else:
#                 return Response("invalid")

# class TrackerView(APIView):
#     global user
#     def get(self,request):
#         # global user
#         tracker = Tracker.objects.filter(customerID=user)
#         serializer = TrackerSerializer(tracker,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         global exst
#         global track
#         global GFRID
#         GFRID =0
#         track = None
#         exst = False
#         serializer = trackerdetailserializers(data=request.data)
#         if serializer.is_valid():
#             # return Response(serializer.data)
#             exst = gfr.objects.filter(tracker=serializer.data['tracker']).exists()
#             # return Response(exst)
#             if exst is True:
#                 track = serializer.data['tracker']
#                 GFRID = gfr.objects.get(tracker=serializer.data['tracker']).id
#                 customer = Customer.objects.first()
#                 refresh = RefreshToken.for_user(customer)
#                 access = str(refresh.access_token)
#                 response = Response()
#                 response.data={
#                     # 'access' : access,
#                     'url' : 'http://127.0.0.1:8000/loadcell/'
#                 }
#                 return response

#             else:
#                 return Response("this tracker not in gfr",status=status.HTTP_404_NOT_FOUND)

# class LoadCellView(APIView):
#     # permission_classes = [IsAuthenticated]
#     def get(self,request):
#         global track
#         global GFRID
#         # global exst
#         # if exst is True:
#         if Loadcell.objects.filter(gfrid=GFRID):
#             data = gfr.objects.get(tracker=track).id
#             loadcell = Loadcell.objects.filter(gfrid=data)
#             gps = Gps.objects.filter(gfrid=data)
#             # serializer= LoadcellSerializer(loadcell,many=True)
#             # return Response(serializer.data)
#             context={'load':loadcell,'gps':gps}
#             return render(request,'tracker/dashboard.html',context)
#         else:
#             return Response("gfrid not connected to loadcell")
        # else: 
        #     return Response("this tracker not in gfr",status=status.HTTP_404_NOT_FOUND)

# def Tracker_Detail(request):
#     global user
#     user = 0

#     r=request.GET.get('json')
#     res = str(r)
#     cus = Customer.objects.get(Customer_Identifier=res)
#     serializer = CustomerSerializers(cus)
#     req = request.POST(serializer.data)
    
#         return Response(serializer.data)

#     if request.method =='POST':
#         serializer = LoginSerializers(data=request.data)
#         if serializer.is_valid():
#             user = Customer.objects.get(Customer_Identifier=serializer.data['Customer_Identifier']).id
#             customer=Customer.objects.filter(Customer_Identifier=serializer.data['Customer_Identifier'],password=serializer.data['password']).exists()
#             if customer is True:
#                 return redirect("http://127.0.0.1:8000/tracker/")
#             else:
#                 return Response("invalid")


# #main1
# @api_view(['GET','POST'])
# def Tracker_Detail(request):
#     global user
#     global GFRID
#     # global username
#     # global password
#     global track
#     # user = 0
#     # GFRID = 0
#     # username = None
#     # password = None
#     # track = None
#     if request.method == 'GET':
#         r=request.GET.get('id')
#         res = str(r)
#         cus = Customer.objects.get(Customer_Identifier=res)
#         serializer = CustomerSerializers(cus)
#         track = request.GET.get('tracker')
#         # username = serializer.data['Customer_Identifier']
#         # password = serializer.data['password']
#         # print(track)
#         response = Response()
#         response.data = {
#             "username" : serializer.data['Customer_Identifier'],
#             "password" : serializer.data['password'],
#             "tracker" : track
#         }

#         return response

#     if request.method =='POST':
#         serializer = LoginSerializers(data=request.data)
#         if serializer.is_valid():
#             # user = Customer.objects.get(Customer_Identifier=username).id
#             customer=Customer.objects.filter(Customer_Identifier=serializer.data['username'],password=serializer.data['password']).exists()
#             # print(username,password,customer)
#             if customer is True:
#                 exst = gfr.objects.filter(tracker=track).exists()
#                 print(track)
#                 if exst is True:
#                     GFRID = gfr.objects.get(tracker=track).id
#                     return Response("http://127.0.0.1:8000/loadcell")
#                     # return redirect("http://127.0.0.1:8000/loadcell")
#                 else:
#                     return Response("this tracker not connected to gfrid")
#             else:
#                 return Response("invalid")


# # class TrackerView(APIView):
# #     global user
# #     def get(self,request):
# #         # global user
# #         tracker = Tracker.objects.filter(customerID=user)
# #         serializer = TrackerSerializer(tracker,many=True)
# #         return Response(serializer.data)
    
# #     def post(self,request):
# #         global exst
# #         global track
# #         global GFRID
# #         GFRID =0
# #         track = None
# #         exst = False
# #         serializer = trackerdetailserializers(data=request.data)
# #         if serializer.is_valid():
# #             # return Response(serializer.data)
# #             exst = gfr.objects.filter(tracker=serializer.data['tracker']).exists()
# #             # return Response(exst)
# #             if exst is True:
# #                 track = serializer.data['tracker']
# #                 GFRID = gfr.objects.get(tracker=serializer.data['tracker']).id
# #                 customer = Customer.objects.first()
# #                 refresh = RefreshToken.for_user(customer)
# #                 access = str(refresh.access_token)
# #                 response = Response()
# #                 response.data={
# #                     # 'access' : access,
# #                     'url' : 'http://127.0.0.1:8000/loadcell/'
# #                 }
# #                 return response

# #             else:
# #                 return Response("this tracker not in gfr",status=status.HTTP_404_NOT_FOUND)

# class LoadCellView(APIView):
#     # permission_classes = [IsAuthenticated]
#     def get(self,request):
#         global track
#         global GFRID
#         # global exst
#         # if exst is True:
#         if Loadcell.objects.filter(gfrid=GFRID):
#             data = gfr.objects.get(tracker=track).id
#             # historical data
#             loadcell = Loadcell.objects.filter(gfrid=data)
#             gps = Gps.objects.filter(gfrid=data)
#             # live data
#             # loadcell_live = Loadcell.objects.filter()
#             # serializer= LoadcellSerializer(loadcell,many=True)
#             # return Response(serializer.data)
#             context={'load':loadcell,'gps':gps}
#             ct = datetime.datetime.now()
#             ts = ct.timestamp()
#             print("timestamp:-", ts)
#             return render(request,'tracker/dashboard.html',context)
#         else:
#             return Response("gfrid not connected to loadcell")

#  #  #main2# # #
# def Tracker_Detail(request):
#     global user
#     user = 0
#     global customer
#     customer = False
#     global GFRID
#     global track
#     global tracke
#     # global username
#     form = LoginForm()
#     if request.method == 'POST':
#         # username = request.GET.get('username')
#         # password = request.GET.get('password')
#         track = request.GET.get('track')
#         # print(track)
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             user = Customer.objects.get(Customer_Identifier=form.data['username']).id
#             tracke = Tracker.objects.filter(customerID=user)
#             # for i in tracke:
#             #     tr = i.tracker
#             #     print(i.tracker)
#             # tracke = Tracker.objects.filter(customerID=user)
#             # context['tracke']=tracke

#             # for i in tracke:
#             #     print(i.tracker)
            
#             # print(tracke.tracker)
            
#             customer = Customer.objects.filter(Customer_Identifier=form.data['username'],password=form.data['password']).exists()

          
#             if customer==True:

#                 exst = gfr.objects.filter(tracker=track).exists()
#                 if exst is True:
#                     GFRID = gfr.objects.get(tracker=track).id
#                     # return Response("http://127.0.0.1:8000/loadcell")
#                     return redirect("http://127.0.0.1:8000/loadcell")
# #                 else:
#                     # return Response("this tracker not connected to gfrid")

#     context = {'form':form}

#     return render(request,'tracker/login.html',context)

# #main3# #
def Tracker_Detail(request):
    global user
    user = 0
    global customer
    customer = False
    global GFRID
    global track
    global tracke
    # global username
    # err = "This tracker is not connected to the gfrid"
    r=request.GET.get('id')
    res = str(r)
    username = Customer.objects.get(Customer_Identifier=res)
    p = Customer.objects.get(Customer_Identifier=res).id
    # pwd = Customer.objects.get(pw)
    pw = Customer.objects.get(id=p)
    pwd = pw.password
    # pwd = Customer.objects.get(password)
    # password = Customer.objects.get(password=res)
    # username = request.GET.get('username')
    # password = request.GET.get('password')
    user = Customer.objects.get(Customer_Identifier=username).id
    tracke = Tracker.objects.filter(customerID=user)
    form = LoginForm()
    if request.method == 'POST':
        track = request.GET.get('tracker')
        # print(track)
        form = LoginForm(request.POST)
        if form.is_valid():
            user = Customer.objects.get(Customer_Identifier=form.data['username']).id
            # track = request.POST.get('tracker',False)
            # print(track)
            customer = Customer.objects.filter(Customer_Identifier=form.data['username'],password=form.data['password']).exists()
          
            if customer==True:

                exst = gfr.objects.filter(tracker=track).exists()
#                 print(track)
                if exst is True:
                    GFRID = gfr.objects.get(tracker=track).id
                    # return Response("http://127.0.0.1:8000/loadcell")
                    return redirect("http://127.0.0.1:8000/loadcell")
                elif(exst is False):
                    err = "This Tracker is not connected to the GFR"
                else:
                    None

    context = {'form':form,'tracker':tracke,'username':username,'pwd':pwd}

    return render(request,'tracker/login.html',context)


# class Tracker_Detail(APIView):
#     # user = 0
#     # GFRID = 0
#     # username = None
#     # password = None
#     # track = None
#     def get(self,request):
#         global user
#         # global username
#         # global password
#         global track
#         r=request.GET.get('id')
#         res = str(r)
#         # username = request.GET.get('username')
#         # password = request.GET.get('password')
#         cus = Customer.objects.get(Customer_Identifier=res)
#         serializer = CustomerSerializers(cus)
#         track = request.GET.get('tracker')
#         # username = serializer.data['Customer_Identifier']
#         # password = serializer.data['password']
#         # print(track)
#         response = Response()
#         response.data = {
#             "username" : serializer.data['Customer_Identifier'],
#             "password" : serializer.data['password'],
#             "tracker" : track
#         }

#         return response

#     def post(self,request):
#         global GFRID
#         serializer = LoginSerializers(data=request.data)
#         if serializer.is_valid():
#             # user = Customer.objects.get(Customer_Identifier=username).id
#             customer=Customer.objects.filter(Customer_Identifier=serializer.data['username'],password=serializer.data['password']).exists()
#             # print(username,password,customer)
#             if customer is True:
#                 exst = gfr.objects.filter(tracker=track).exists()
#                 print(track)
#                 if exst is True:
#                     GFRID = gfr.objects.get(tracker=track).id
#                     # return Response("http://127.0.0.1:8000/loadcell")
#                     return redirect('http://127.0.0.1:8000/loadcell')
#                 else:
#                     return Response("this tracker not connected to gfrid")
#             else:
#                 return Response("invalid")


# class TrackerView(APIView):
#     global user
#     def get(self,request):
#         # global user
#         tracker = Tracker.objects.filter(customerID=user)
#         serializer = TrackerSerializer(tracker,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         global exst
#         global track
#         global GFRID
#         GFRID =0
#         track = None
#         exst = False
#         serializer = trackerdetailserializers(data=request.data)
#         if serializer.is_valid():
#             # return Response(serializer.data)
#             exst = gfr.objects.filter(tracker=serializer.data['tracker']).exists()
#             # return Response(exst)
#             if exst is True:
#                 track = serializer.data['tracker']
#                 GFRID = gfr.objects.get(tracker=serializer.data['tracker']).id
#                 customer = Customer.objects.first()
#                 refresh = RefreshToken.for_user(customer)
#                 access = str(refresh.access_token)
#                 response = Response()
#                 response.data={
#                     # 'access' : access,
#                     'url' : 'http://127.0.0.1:8000/loadcell/'
#                 }
#                 return response

#             else:
#                 return Response("this tracker not in gfr",status=status.HTTP_404_NOT_FOUND)

# # #both live and historical 
# class LoadCellView(APIView):
#     # permission_classes = [IsAuthenticated]
#     def get(self,request):
#         global track
#         global GFRID

#         if Loadcell.objects.filter(gfrid=GFRID):
#             data = gfr.objects.get(tracker=track).id
#             # historical data
#             loadcell = Loadcell.objects.filter(gfrid=data)
#             for i in loadcell:
#                 ldh_ts = i.ts
#                 print(ldh_ts)
#             ldh_dt = dt.fromtimestamp(ldh_ts)
#             gps = Gps.objects.filter(gfrid=data)
#             for i in gps:
#                 gpsh_ts = i.ts
#                 print(gpsh_ts)
#             gpsh_dt = dt.fromtimestamp(gpsh_ts)

#             # live data
#             loadcell_live = Loadcell.objects.filter(gfrid=data).latest('ts')
#             ld_lv = Loadcell.objects.filter(ts=loadcell_live.ts)
#             for i in ld_lv:
#                 ldl_ts = i.ts
#             ldl_dt = dt.fromtimestamp(ldl_ts)

#             gps_live = Gps.objects.filter(gfrid=data).latest('ts')
#             gps_lv = Gps.objects.filter(ts=gps_live.ts)
#             for i in gps_lv:
#                 gpsl_ts = i.ts
#             gpsl_dt = dt.fromtimestamp(gpsl_ts)
        
#             context={'load':loadcell,'gps':gps,'load_live':ld_lv,'gps_live':gps_lv,'ldh_ts':ldh_dt,'gpsh_ts':gpsh_dt,'ldl_ts':ldl_dt,'gpsl_ts':gpsl_dt}
#             ct = datetime.datetime.now()
#             ts = ct.timestamp()
#             print(ts)
#             # dt_object = dt.fromtimestamp(ts)
#             # print("timestamp:-", dt_object)
#             return render(request,'tracker/dashboard.html',context)
#         else:
#             return Response("gfrid not connected to loadcell")

# #live
class LoadCellLiv(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self,request):
        global track
        global GFRID

        if Loadcell.objects.filter(gfrid=GFRID):
            data = gfr.objects.get(tracker=track).id

            # live data
            loadcell_live = Loadcell.objects.filter(gfrid=data).latest('ts')
            ld_lv = Loadcell.objects.filter(ts=loadcell_live.ts)
            for i in ld_lv:
                ldl_ts = i.ts
            ldl_dt = dt.fromtimestamp(ldl_ts)

            gps_live = Gps.objects.filter(gfrid=data).latest('ts')
            gps_lv = Gps.objects.filter(ts=gps_live.ts)
            for i in gps_lv:
                gpsl_ts = i.ts
            gpsl_dt = dt.fromtimestamp(gpsl_ts)
        
            context={'load_live':ld_lv,'gps_live':gps_lv,'ldl_ts':ldl_dt,'gpsl_ts':gpsl_dt}
            
            return render(request,'tracker/livedata.html',context)
        else:
            return Response("gfrid not connected to loadcell")


# # #historical
class LoadCellHist(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self,request):
        global track
        global GFRID

        if Loadcell.objects.filter(gfrid=GFRID):
            data = gfr.objects.get(tracker=track).id
            # historical data
            loadcell = Loadcell.objects.filter(gfrid=data)
            for i in loadcell:
                ldh_ts = i.ts
                print(ldh_ts)
            ldh_dt = dt.fromtimestamp(ldh_ts)

            gps = Gps.objects.filter(gfrid=data)
            for i in gps:
                gpsh_ts = i.ts
                print(gpsh_ts)
            gpsh_dt = dt.fromtimestamp(gpsh_ts)


            context={'load':loadcell,'gps':gps,'ldh_ts':ldh_dt,'gpsh_ts':gpsh_dt}
    
            return render(request,'tracker/history.html',context)
        else:
            return Response("gfrid not connected to loadcell")


