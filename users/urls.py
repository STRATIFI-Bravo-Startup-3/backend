from django.urls import path
from .views import (InfluencerSignupView,
 BrandSignupView, EmployeeSignupView,
 CustomAuthToken, LogoutView, BrandOnlyView, InfluencerOnlyView, EmployeeOnlyView)

urlpatterns=[
    path('signup/influencer/', InfluencerSignupView.as_view()),
    path('signup/brand/', BrandSignupView.as_view()),
    path('signup/employee/', EmployeeSignupView.as_view()),
    path('login/',CustomAuthToken.as_view(), name='auth-token'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
    path('influencer/dashboard/', InfluencerOnlyView.as_view(), name='influencer-dashboard'),
    path('brand/dashboard/', BrandOnlyView.as_view(), name='brand-dashboard'),
    path('employee/dashboard/', EmployeeOnlyView.as_view(), name='employee-dashboard'),
]