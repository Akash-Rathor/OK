
from django.urls import path,include
# from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from accounts import views
urlpatterns = [

    path('', views.homepage,name="home"),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view(),name="logout"),
    path('dashboard',views.dashboard,name='dashboard'),
    path("404/",views.doesnotexist,name="doesnotexist"),
    path("<str:path>/",views.redirecting,name="redirecting"),
]

