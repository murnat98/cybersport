# Generated by Django 2.0.1 on 2018-02-05 21:10

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('tournaments', '0005_auto_20180204_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournaments',
            name='game_uuid',
            field=models.UUIDField(choices=[(uuid.UUID('184fb5ed-789a-4058-8605-88564074e749'), 'dalm'),
                                            (uuid.UUID('bd8901da-51bb-4efb-9154-153d0f574974'), 'фвы'),
                                            (uuid.UUID('7b3bc1b8-e180-4102-893d-8ceb6d0e15fa'), 'asf'),
                                            (uuid.UUID('fa74bfe8-424b-4554-8f2b-73aff21f1055'), 'tourn'),
                                            (uuid.UUID('e93cc203-2415-46a8-ba88-1f05f40fce8c'), 'asd')],
                                   verbose_name='Игра'),
        ),
    ]
