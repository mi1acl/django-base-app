
from django.urls import path
from .views import SignupPageView

urlpatterns = [
    # Django Admin
    path('signup/', SignupPageView.as_view(), name='signup'),

]
