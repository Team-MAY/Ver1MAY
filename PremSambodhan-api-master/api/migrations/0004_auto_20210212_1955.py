# Generated by Django 3.1.6 on 2021-02-12 19:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_auto_20210212_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='')),
                ('type', models.CharField(choices=[('Image', 'Image'), ('Video', 'Video')], max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.CharField(default='mail@mail.com', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(related_name='Friends', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default='1221.jpg', upload_to=''),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story', models.ManyToManyField(related_name='Story', to='api.StoryData')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]