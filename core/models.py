from django.db import models


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DataTimeField()
    updated = models.DataTimeField()

    class Meta:
        abstarct = True

