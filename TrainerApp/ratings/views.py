from rest_framework import viewsets
from TrainerApp.ratings.models import Rating
from TrainerApp.ratings.serializers import RatingSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from TrainerApp.common.mixin import RedirectOnUnAuthMixin


class RatingViewSet(RedirectOnUnAuthMixin, viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'], url_path='user-rating')
    def retrieve_user_rating(self, request, pk=None):

        user_id = request.user.pk
        trainer_id = pk
        rating = Rating.objects.filter(user=user_id, trainer=trainer_id).first()

        if rating:
            return Response({'rating': rating.rating})
        return Response({'rating': None})