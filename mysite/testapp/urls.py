from django.urls import path

from testapp import views

urlpatterns=[

    path('',views.studentList.as_view(), name= 'student_list'),
    path('create/', views.createStudent.as_view(), name= 'student_create'),
    path('update/<int:pk>/', views.updateStudent.as_view(), name='student_update'),
    path('delete/<int:pk>/', views.deleteStudent.as_view(), name='student_delete'),
    path('<int:pk>/',views.getOnlyStudent.as_view(),name='student_byid'),

    ]