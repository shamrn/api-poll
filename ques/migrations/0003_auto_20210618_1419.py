# Generated by Django 2.2.10 on 2021-06-18 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ques', '0002_auto_20210618_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(unique=True, verbose_name='Уникальный идентификатор')),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('Один выбранный вариант', 'Один выбранный вариант'), ('Несколько выбранных вариантов', 'Несколько выбранных вариантов'), ('Свой вариант ответа', 'Свой вариант ответа')], help_text='Если вы выбрали один или несколько вариантов ответа, заполните поля "описание выбора",если вы выбрали "свой вариант ответа", не заполняйте это поле', max_length=55, verbose_name='Тип вопроса'),
        ),
        migrations.CreateModel(
            name='UserPoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ques.Poll')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ques.UserId')),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswerQues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('ques_choices', models.ManyToManyField(to='ques.QuesChoices')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ques.Question')),
                ('user_poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ques.UserPoll')),
            ],
        ),
    ]