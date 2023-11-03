# api/urls.py

from django.urls import path
from .views import (
    AnimalsListView,
    AnimalsSearchListView
)
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
    path('animals/search/<str:animals_name>', AnimalsSearchListView.as_view(), name='aniamls-search-name'),
    path('animals/', AnimalsListView.as_view(), name='animals-a-z-list'),
]
