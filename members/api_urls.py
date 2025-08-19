from rest_framework import routers
from .api_views import MemberViewSet, MembershipPlanViewSet

router = routers.DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'plans', MembershipPlanViewSet)

urlpatterns = router.urls
