from django.urls import path
from Users_App import views

# Template Urls
app_name = "Users_App"

urlpatterns = [
  path('register/',views.register,name="register"),
  path('user_login/',views.user_login,name='user_login'),
  
]