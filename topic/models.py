from django.db import models
from user.models import User


# Create your models here.
class TopicRecord(models.Model):
    limit_num_choices = (
        (1, '限1人'),
        (2, '限2人'),
        (3, '限3人'),
    )

    status_choices = (
        (1, '未选'),
        (2, '已选'),
    )

    accept_choices = (
        (0, '等待命题老师和教学秘书确认中'),
        (1, '命题教师已确认选题，等待教秘确认'),
        (2, '选题通过'),
    )

    title = models.CharField(max_length=100, blank=False, verbose_name='题目')
    detail = models.TextField('描述')
    chosen_num = models.SmallIntegerField(verbose_name="已选人数", default=0)
    limit_num = models.SmallIntegerField(choices=limit_num_choices, blank=False, verbose_name='限选人数')
    release_time = models.DateTimeField("出题时间", blank=True, null=True, auto_now=True)
    last_edit_time = models.DateTimeField("最后编辑时间", blank=True, null=True, auto_now_add=True)
    status = models.SmallIntegerField(choices=status_choices, default=1, verbose_name='选题状态')
    accept = models.SmallIntegerField(choices=accept_choices, default=0, verbose_name='确认状态')

    class Meta:
        verbose_name = '题目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Annex(models.Model):
    file = models.FileField(upload_to="./media/", blank=True, null=True)
    detail = models.TextField('描述')


class Annex2Topic2User(models.Model):
    annex_id = models.ForeignKey(Annex, on_delete=models.CASCADE)
    topic_id = models.ForeignKey(TopicRecord, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Topic2User(models.Model):
    topic_id = models.ForeignKey(TopicRecord, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '题目用户对应关系'
        verbose_name_plural = verbose_name
