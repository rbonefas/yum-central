from django.urls import re_path as url
from .views import *
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^display_Restaurant$', display_Restaurant, name='display_Restaurant'),
    url(r'^display_Employee$', display_Employee, name='display_Employee'),
    url(r'^display_Location$', display_Location, name='display_Location'),
    url(r'^display_Financial$', display_Financial, name='display_Financial'),
    url(r'^display_Cost$', display_Cost, name='display_Cost'),
    url(r'^display_Rewards$', display_Rewards, name='display_Rewards'),
    url(r'^display_Restaurant_Report', display_Restaurant_Report, name='display_Restaurant_Report'),
    url(r'^display_Employee_Report', display_Employee_Report, name='display_Employee_Report'),
    url(r'^display_Financial_Report', display_Financial_Report, name='display_Financial_Report'),
    url(r'^display_Rewards_Report', display_Rewards_Report, name='display_Rewards_Report'),
    url(r'^display_Location_Report', display_Location_Report, name='display_Location_Report'),


    url(r'^add_Restaurant$', add_Restaurant, name='add_Restaurant'),
    url(r'^add_Employee$', add_Employee, name='add_Employee'),
    url(r'^add_Location$', add_Location, name='add_Location'),
    url(r'^add_Financial$', add_Financial, name='add_Financial'),
    url(r'^add_Cost$', add_Cost, name='add_Cost'),
    url(r'^add_Rewards', add_Rewards, name='add_Rewards'),


    url(r'^Restaurant/edit_item/(?P<pk>\d+)$', edit_Restaurant, name="edit_Restaurant"),
    url(r'^Employee/edit_item/(?P<pk>\d+)$', edit_Employee, name="edit_Employee"),
    url(r'^Location/edit_item/(?P<pk>\d+)$', edit_Location, name="edit_Location"),
    url(r'^Financial/edit_item/(?P<pk>\d+)$', edit_Financial, name="edit_Financial"),
    url(r'^Cost/edit_item/(?P<pk>\d+)$', edit_Cost, name="edit_Cost"),
    url(r'^Rewards/edit_item/(?P<pk>\d+)$', edit_Rewards, name="edit_Rewards"),

    url(r'^Restaurant/delete/(?P<pk>\d+)$', delete_Restaurant, name="delete_Restaurant"),
    url(r'^Employee/delete/(?P<pk>\d+)$', delete_Employee, name="delete_Employee"),
    url(r'^Location/delete/(?P<pk>\d+)$', delete_Location, name="delete_Location"),
    url(r'^Financial/delete/(?P<pk>\d+)$', delete_Financial, name="delete_Financial"),
    url(r'^Cost/delete/(?P<pk>\d+)$', delete_Cost, name="delete_Cost"),
    url(r'^Rewards/delete/(?P<pk>\d+)$', delete_Rewards, name="delete_Rewards")


]