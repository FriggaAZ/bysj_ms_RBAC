from topic.models import TopicRecord, Topic2User
from django.forms import ModelForm


#
# class CreateTopicForm(forms.Form):
#     limit_num_choices = (
#         (1, '限1人'),
#         (2, '限2人'),
#         (3, '限3人'),
#     )
#
#     status_choices = (
#         (1, '未选'),
#         (2, '已选'),
#     )
#     accept_choices = (
#         (0, '等待命题老师和教学秘书确认中'),
#         (1, '命题教师已确认选题，等待教秘确认'),
#         (2, '选题通过'),
#     )
#
#     title = forms.CharField(label='毕业设计题目', max_length=100)
#     detail = forms.Textarea()
#     # chosen_num = forms.IntegerField(label='已选人数', default=0)
#     limit_num = forms.ChoiceField(label='限选人数', choices=limit_num_choices)
#     release_time = forms.DateTimeField(label='出题时间')
#     status = forms.ChoiceField(label='题目被选择状态', choices=status_choices, default=1)
#     accept = forms.ChoiceField(label='题目确认状态', choices=accept_choices, default=0)

class TopicRecordForm(ModelForm):
    class Meta:
        model = TopicRecord
        fields = [
            'title',
            'detail',
            # 'chosen_num',
            'limit_num',
            # 'release_time'
            # 'status',
            # 'accept'
        ]


class Topic2UserForm(ModelForm):
    class Meta:
        model = Topic2User
        fields = [
            'topic_id',
            'user_id',
        ]
