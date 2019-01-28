# Generated by Django 2.1.3 on 2018-12-17 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweetmodel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetmodel',
            name='tweet',
            field=models.CharField(default='', max_length=140),
        ),
        migrations.AddField(
            model_name='tweetpicturemodel',
            name='picture',
            field=models.ImageField(default='media/kitten.jpg', upload_to='media/'),
        ),
        migrations.AddField(
            model_name='tweetpicturemodel',
            name='tweet',
            field=models.CharField(default='', max_length=70),
        ),
    ]
