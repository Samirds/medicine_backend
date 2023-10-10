from django.urls import path

from . views import Registration, Login, Profile


urlpatterns = [
    path('register/', Registration.as_view()),
    path('login/', Login.as_view()), 
    path('profile/', Profile.as_view())
]
    # path('login/', Login.as_view()),
    # path('profile/', Profile.as_view()),
    # path('signout/', Signout.as_view()),
    # path('newolgout/', newLogout.as_view()),
    # path('home/', HomePage.as_view()),
    # path('logoutview/', LogoutView.as_view(), name='auth_logout'),
     
    
