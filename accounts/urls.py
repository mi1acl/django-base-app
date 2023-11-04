
from django.urls import path
from .views import SignupPageView
from .forms import CustomUserCreationForm

urlpatterns = [
    # Django Admin
    path('signup/', SignupPageView.as_view(), name='signup'),

]
