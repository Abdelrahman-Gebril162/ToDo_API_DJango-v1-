from django.urls import path
from . import views 
urlpatterns = [
    path('',views.ApiOverView , name="overview"),
    path('task_list/',views.tasklist,name="tasklist"),
    path('task_details/<str:pk>/',views.taskDetail,name="taskdetail"),
    path('task_create/',views.taskCreate,name="taskcreate"),
    path('task_update/<str:pk>/',views.taskUpdate,name="taskupdate"),
    path('task_delete/<str:pk>/',views.taskDelete,name="taskdelete"),
]