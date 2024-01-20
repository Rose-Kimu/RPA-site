from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('', views.index, name='index'),
     path('', views.loginUser, name="login_user"),

    path('create_report/', views.createReport, name="create_report"),

    path('add_report/', views.addReportBtn, name="add_report_btn"),

    path('register/', views.registerUser, name="register_user"),

     path('view_reports/', views.viewAllReports, name="view_all_reports")

   



]