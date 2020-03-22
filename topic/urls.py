from django.urls import path, include
from django.conf.urls import url
from topic import views
from user.views import RegisterView, LoginView

urlpatterns = [
    path('', views.show_all_topic, name="show_all_topic"),
    path('index/', views.show_index, name="show_my_topic"),
    path('test_create_topic/', views.test_create_topic, name="test_create_topic"),
    # url(r"^create/$", views.create_question, name="create_topic"),
    # url(r'^edit-(\d+)/$', views.edit_question, name="edit_topic"),
    # url(r'^show-(\d+)/$', views.show_question, name="show_topic"),

]
