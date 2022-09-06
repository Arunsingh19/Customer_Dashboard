"""Asset URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from tracker import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.getRoute),
    # path('data/',views.getData),
    # path('data/gfr/',views.gfr_detail),
    # path('gfr/',views.gfr_detail),
    # path('tracker/',views.TrackerView.as_view()),
    path('',views.Tracker_Detail),
    path('loadcell/',views.LoadCellLiv.as_view()),
    path('loadcell/history',views.LoadCellHist.as_view())
    # path('login/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    # path('login/refresh',TokenRefreshView.as_view(),name='token_refresh'),
]
