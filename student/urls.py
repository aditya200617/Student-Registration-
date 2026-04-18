from django.contrib import admin
from django.urls import path,include
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.index,name="student"),
    path('',views.add_show,name='addandshow'),
    path('delete_student/<int:id>/', views.delete_student, name='delete_student'),
    path('update_student/<int:id>/', views.update_student, name="update_student"),
    ]

