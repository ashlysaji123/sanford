from votings.models import Voting, VotingItem

from .serializers import VotingSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_voting(request, pk):
    voting_item = VotingItem.objects.get(pk=pk)
    serializer = VotingSerializer(data=request.data, context={"request": request}) 
    if serializer.is_valid():
        user = request.user
        if Voting.objects.filter(user=user,voting_item=voting_item).exists():
            response = {
                "status": 400, 
                "message": "Already voted",
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            serializer.save(user=user,voting_item=voting_item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        response = {"status": 400, "message": serializer.errors}
        return Response(response, status=status.HTTP_200_OK)

