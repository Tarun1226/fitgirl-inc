# Generated by Django 2.0 on 2018-09-30 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20180923_1359'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ValidUser',
            new_name='RegisterUser',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='age_group',
            field=models.IntegerField(choices=[(1, '8-10'), (2, '11-13')], default=None),
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='day_phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='eve_phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='school',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='zip',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
