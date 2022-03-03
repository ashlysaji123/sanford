from rest_framework.generics import ListAPIView

from rewards.models import RewardPoint

from .serializers import RewardPointSerializer


class RewardSummaryView(ListAPIView):
	"""
    View to list all Reward Points assigned with current user
    """
	serializer_class = RewardPointSerializer

	def get_queryset(self):
		return RewardPoint.objects.filter(user=self.request.user,is_deleted=False)
