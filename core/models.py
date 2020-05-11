from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # auto_now = model을 save 할 때 date랑 time을 기록함
    # auto_now_add = model을 생성할 때 마다 수시로 업데이트 기록
    # Boolean 값을 True로 했을 시

    class Meta:
        abstract = True
        """ 
        core의 모델이 데이터베이스에
        등록되지 않기 위한 클래스 
        """
