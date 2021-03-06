# Generated by Django 3.2.3 on 2021-07-23 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210720_1647'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='document',
            new_name='business_strategy',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='eaddress',
            new_name='email_address',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='fname',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='lname',
            new_name='lastname',
        ),
        migrations.RemoveField(
            model_name='application',
            name='zip',
        ),
        migrations.AddField(
            model_name='application',
            name='zip_code',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='application',
            name='city',
            field=models.CharField(max_length=150),
        ),
    ]
