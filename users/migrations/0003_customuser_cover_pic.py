# Generated by Django 2.1.3 on 2019-01-18 10:51

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190115_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='cover_pic',
            field=stdimage.models.StdImageField(blank=True, upload_to='cover_pic/'),
        ),
    ]
