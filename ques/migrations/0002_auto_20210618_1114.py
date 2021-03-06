# Generated by Django 2.2.10 on 2021-06-18 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ques', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poll',
            options={'verbose_name': 'Опрос', 'verbose_name_plural': 'Опросы'},
        ),
        migrations.AlterModelOptions(
            name='queschoices',
            options={'verbose_name': 'Выбор ответа', 'verbose_name_plural': 'Выбор ответа'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.AlterField(
            model_name='poll',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='start_date',
            field=models.DateTimeField(blank=True, help_text='Учтите, после заполнения даты, изменить опрос вы не сможете.', null=True, verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='queschoices',
            name='desc',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Описание выбора'),
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('Один выбранный вариант', 'Один выбранный вариант'), ('Несколько выбранных вариантов', 'Несколько выбранных вариантов'), ('Свой вариант ответа', 'Свой вариант ответа')], help_text='Если вы выбрали один или несколько вариантов ответа, заполните поля "описание выбора",если вы выбрали "свой вариант ответа", не заполняйте поля "описание выбора"', max_length=55, verbose_name='Тип вопроса'),
        ),
    ]
