from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import render
from datetime import datetime as dt
from tracker.models import Gps, Loadcell, Tracker, gfr, Customer

class Tracker_Detail(APIView):
    def get(self,request):
        global user
        user = 0
        global customer
        customer = False
        global GFRID
        global cust_tracker
        global tracke

        # #data
        cust_id = "JIVS"
        cust_pass = "12345678"
        cust_tracker = "JIVSJIS1GFR4418"

        if(Customer.objects.filter(Customer_Identifier=cust_id).exists()):
            username = Customer.objects.get(Customer_Identifier=cust_id)


            user = Customer.objects.get(Customer_Identifier=username).id
            tracke = Tracker.objects.filter(customerID=user)

            user = Customer.objects.get(Customer_Identifier=username).id

            customer = Customer.objects.filter(Customer_Identifier=username,password=cust_pass).exists()

            if customer==True:

                exst = gfr.objects.filter(tracker=cust_tracker).exists()
#
                if exst is True:
                    GFRID = gfr.objects.get(tracker=cust_tracker).id

                    if Loadcell.objects.filter(gfrid=GFRID):
                        data = gfr.objects.get(tracker=cust_tracker).id

                    # live data
                        loadcell_live = Loadcell.objects.filter(gfrid=data).latest('ts')
                        ld_lv = Loadcell.objects.filter(ts=loadcell_live.ts)
                        # serializer =llserializer(loadcell_live)

                        for i in ld_lv:
                            ldl_ts = i.ts
                        ldl_dt = dt.fromtimestamp(ldl_ts)

                        gps_live = Gps.objects.filter(gfrid=data).latest('ts')
                        gps_lv = Gps.objects.filter(ts=gps_live.ts)
                        # serializer = glserializer(gps_live)

                    # print(gps_lv)
                        for i in gps_lv:
                            gpsl_ts = i.ts
                        gpsl_dt = dt.fromtimestamp(gpsl_ts)
                        # return Response(serializer.data)
                        context={'load_live':ld_lv,'gps_live':gps_lv,'ldl_ts':ldl_dt,'gpsl_ts':gpsl_dt}

                        return render(request,'tracker/livedata.html',context)
                    else:
                        return Response("gfrid not connected to loadcell",status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response("enter a valid tracker",status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response("Enter a valid password",status=status.HTTP_401_UNAUTHORIZED)


        return Response("user not found",status=status.HTTP_204_NO_CONTENT)


# # #historical
class LoadCellHist(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self,request):
        global cust_tracker
        global GFRID
        print(GFRID)
        if Loadcell.objects.filter(gfrid=GFRID):
            data = gfr.objects.get(tracker=cust_tracker).id
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