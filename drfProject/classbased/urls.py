from django.urls import path
from.views import *

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("stud", StudentViewSet)


urlpatterns = router.urls


# urlpatterns = [

#    path('hello/', HelloWorldView.as_view(), name="hello_world"),
#    path('stud/', StudentView.as_view(), name="hello_world"),


# ]