from django.urls import path
from .import views
from .views import StudentList

urlpatterns = [
   path('welcome/',views.Welcome, name='welcome'),
   path('show/',views.Show, name='show'),
   path('list/',views.list_view),
   path('list2/', StudentList.as_view())

]