# Generated by Django 3.0.3 on 2020-10-01 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_bmiuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='BMIUser',
        ),
        migrations.DeleteModel(
            name='UserDetail',
        ),
    ]