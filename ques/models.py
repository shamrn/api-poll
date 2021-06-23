from django.core.exceptions import ValidationError
from django.db import models


class Poll(models.Model):
    """Основная таблица опроса"""
    name = models.CharField('Название опроса', max_length=200)
    desc = models.TextField('Описание')
    start_date = models.DateTimeField('Дата начала', null=True, blank=True,
                                      help_text='Учтите, после заполнения даты, изменить опрос вы не сможете.')
    end_date = models.DateTimeField('Дата окончания', null=True, blank=True)

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.name

    def clean(self,*args,**kwargs):
        if Poll.objects.filter(pk=self.pk).exists():
            if self.start_date and Poll.objects.filter(pk=self.pk,start_date__isnull=False):
                raise ValidationError({'start_date': 'Дата уже заполнена, опрос изменить невозможно'})
        if self.start_date and not self.end_date:
            raise ValidationError({'end_date':'Заполните дату окончания опроса'})



class Question(models.Model):
    """Таблица вопроса"""
    CHOICES_TYPE = (
        ('Один выбранный вариант', 'Один выбранный вариант'),
        ('Несколько выбранных вариантов', 'Несколько выбранных вариантов'),
        ('Свой вариант ответа', 'Свой вариант ответа'),
    )
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='question', verbose_name='Опрос')
    desc = models.TextField('Текст вопроса')
    type = models.CharField('Тип вопроса', choices=CHOICES_TYPE, max_length=55,
                            help_text='Если вы выбрали один или несколько вариантов ответа, заполните поля "описание выбора",'
                                      'если вы выбрали "свой вариант ответа", не заполняйте это поле')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.desc


class QuesChoices(models.Model):
    """Таблица варинтов ответа"""
    question = models.ForeignKey(Question, related_name='ques_choices', on_delete=models.CASCADE)
    desc = models.CharField('Описание выбора', null=True, blank=True, max_length=200)

    class Meta:
        verbose_name = 'Выбор ответа'
        verbose_name_plural = 'Выбор ответа'

    def __str__(self):
        return self.desc


class UserId(models.Model):
    """Таблица пользователей"""
    user_id = models.IntegerField('Уникальный идентификатор пользователя', unique=True)

    class Meta:
        verbose_name = 'Опрос пользователей'
        verbose_name_plural = 'Опросы пользователей'

    def __str__(self):
        return f'{self.user_id} - id пользователя'


class UserPoll(models.Model):
    """Таблица проходящяго опроса пользователя"""
    user_id = models.ForeignKey(UserId, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name='Опрос')

    class Meta:
        verbose_name = 'Пройденный опрос'
        verbose_name_plural = 'Пройденный опрос'

    def __str__(self):
        return self.poll.name


class UserAnswerQues(models.Model):
    """Таблица вопроса и ответа/ответов на него пользователем"""
    user_poll = models.ForeignKey(UserPoll, on_delete=models.CASCADE, verbose_name='Опрос', related_name='user_poll')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    text = models.TextField(null=True, blank=True, verbose_name='Свой вариант ответа')
    ques_choices = models.ManyToManyField(QuesChoices, null=True, blank=True, verbose_name='Выбранный ответ/ответы')

    class Meta:
        verbose_name = 'Ответ пользователя'
        verbose_name_plural = 'Ответ пользователя'

    def __str__(self):
        return self.question.desc
