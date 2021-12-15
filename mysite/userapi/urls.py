from django.urls import path

from userapi import views

urlpatterns = [

    path('', views.userList.as_view(), name= 'user_list' ),
    path('<int:pk>/', views.getOnlyUser.as_view(), name= 'user_byid'),
    path('create/', views.createUser.as_view(), name='user_create'),
    path('update/<int:pk>', views.updateUser.as_view(), name='user_update'),
    path('delete/<int:pk>', views.deleteUser.as_view(), name='delete_user')
    
]