from django.urls import path
from .views import Task_View, Create_Task, Delete_Task
from .views import Task_Update_View, task_detail
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', Task_View.as_view(), name='home_page'),
    path('task/create/', Create_Task.as_view(), name='new_task'),
    path('task/<int:pk>/delete/', Delete_Task.as_view(), name='delete_task'),
    path('task/<int:pk>/update/', Task_Update_View.as_view(), name='update_task'),
    path('task/<int:id>/detail/', task_detail, name='task_detail')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)