# Generated by Django 3.1.6 on 2021-02-15 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('username', models.CharField(max_length=100)),
                ('user_id', models.IntegerField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserTweet',
            fields=[
                ('message', models.CharField(max_length=1000)),
                ('tweet_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='user.twitteruser')),
            ],
        ),
    ]
