# Generated by Django 2.1.5 on 2019-05-20 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, default=None, max_length=100, unique=True),
        ),
    ]
