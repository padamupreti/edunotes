# Generated by Django 4.2.5 on 2023-10-01 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='description',
            field=models.CharField(default='default description', max_length=150),
            preserve_default=False,
        ),
    ]
