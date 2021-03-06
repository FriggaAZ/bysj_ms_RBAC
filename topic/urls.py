from django.urls import path, include
from django.conf.urls import url
from topic import views
from user.views import RegisterView, LoginView

urlpatterns = [
    path('', views.show_all_topic, name="show_all_topic"),
    path('index/', views.show_index, name="show_my_topic"),
    path('create/', views.test_create_topic, name="create_topic"),
    path('upload_file/', views.upload_file, name="upload_file"),
    url(r'^show-(\d+)/$', views.topic_detail, name="topic_detail"),
    url(r'^delete-(\d+)/$', views.delete_topic, name="delete_topic"),

    # url(r'^edit-(\d+)/$', views.edit_topic, name="edit_topic"),
    # url(r"^create/$", views.test_create_topic, name="create_topic"),


]
