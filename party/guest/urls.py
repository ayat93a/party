import jwt
from guest.api.viewset import GuestListAPIView , GuestRetrieveUpdateDestroyAPIView
from django.urls import path
from rest_framework_simplejwt import views as jwt_view


urlpatterns =[
    path('list' , GuestListAPIView.as_view(), name ='list'),
    path('<int:pk>' , GuestRetrieveUpdateDestroyAPIView.as_view(), name='detail'),
    path('token' , jwt_view.TokenObtainPairView.as_view() , name = 'token_obtain'),
    path('refresh' , jwt_view.TokenRefreshView.as_view() , name = 'refresh')
]



# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NDAxOTUyNiwiaWF0IjoxNjUzOTMzMTI2LCJqdGkiOiI2OTEwMjNjZGZmNmQ0OWYyYmNiNjEyMTdkM2Y3NTljMSIsInVzZXJfaWQiOjF9.MmKTrtwHQjka_UoYB34YXMsPUJ-7jkr8YfvgIr_JUiw",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUzOTMzNDI2LCJpYXQiOjE2NTM5MzMxMjYsImp0aSI6ImFlM2IxNzQzNWRjZjQzMjliZmE5ZmU0YzFkMjdjY2Y0IiwidXNlcl9pZCI6MX0.6OMZxTayd1GFjdjWLrsItXwNKsdfadTUN2gn_89gC5I"
# }