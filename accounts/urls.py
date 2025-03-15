from django.urls import path
from .views import SignupView, LoginView, login_page, signup_page, dashboard_page

urlpatterns = [
    #path('signup/', SignupView.as_view(), name='signup'),
    #path('login/', LoginView.as_view(), name='login'),
     # API Endpoints
    path('api/auth/signup/', SignupView.as_view(), name='signup'),
    path('api/auth/login/', LoginView.as_view(), name='login'),

    # Frontend Endpoints
    path('login/', login_page, name='login_page'),
    path('signup/', signup_page, name='signup_page'),
    path('dashboard/', dashboard_page, name='dashboard_page'),
]