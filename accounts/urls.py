from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import UserLoginView

urlpatterns = [


    path('logout/', LogoutView.as_view(next_page="memory_list"), name='logout'),

    path('login/', UserLoginView.as_view(), name='login'),

]
