from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register("users", views.UserView)
router.register("ret", views.RetrieveView, basename="ret")



urlpatterns = [
    *router.urls,
]