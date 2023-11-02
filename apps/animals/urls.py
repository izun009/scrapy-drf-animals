# api/urls.py

from django.urls import path
from .views import AnimalsViewSet
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView
# )

urlpatterns = [
    # path('data/retrieve/', DataRetrieveView.as_view(), name='data-retrieve'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('animals/', AnimalsViewSet.as_view(), name='animals-a-z-list'),
]
