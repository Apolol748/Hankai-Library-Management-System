from django.urls import path, include
from . import views

urlpatterns = [
    path('borrow/', views.home, name='home'),
    path('borrow/bookofprinciplewang1', views.wzb1,name='wzb1'),
    path('borrow/bookofprinciplewang2', views.wzb2,name='wzb2'),
    path('borrow/bookofprinciplewang3', views.wzb3,name='wzb3'),
    path('to_borrow/bookofprinciplewang1', views.borrow_wzb1,name='borrow_wzb1'),
    path('to_borrow/bookofprinciplewang2', views.borrow_wzb2,name='borrow_wzb2'),
    path('to_borrow/bookofprinciplewang3', views.borrow_wzb3,name='borrow_wzb3'),
    path('',views.introduction, name='introduction'),
    path('to_borrow/', views.to_borrow, name='to_borrow'),
    path('to_return/', views.to_return, name='to_return'),
]