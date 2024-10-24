from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register("users", views.UserView)


urlpatterns = [
    *router.urls,
]