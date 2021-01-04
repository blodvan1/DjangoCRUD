from django.conf.urls import url
from . import views
from django.urls import path, include



urlpatterns = [
    #path('', views.IndexGenericView.as_view(), name = 'main'),
    url(r'^$', views.IndexGenericView.as_view(), name = 'main'),
    url(r'^employees/profile/list/$', views.EmployeeListView.as_view(), name='employee'),
    url(r'^employees/profile/create/$', views.EmployeeCreateView.as_view(), name='employee_create'),
    url(r'^employees/(?P<pk>[0-9]+)/profile/update/$', views.EmployeeUpdateView.as_view(), name='employee_update'),
    url(r'^employees/(?P<pk>[0-9]+)/profile/delete/$', views.EmployeeDeleteView.as_view(), name='employee_delete'),
]