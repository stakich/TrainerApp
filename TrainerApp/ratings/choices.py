from django.db import models


class RatingChoices(models.IntegerChoices):
    RATING_1 = 1, '1 Star'
    RATING_2 = 2, '2 Stars'
    RATING_3 = 3, '3 Stars'
    RATING_4 = 4, '4 Stars'
    RATING_5 = 5, '5 Stars'
