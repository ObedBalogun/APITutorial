# Generated by Django 2.0.7 on 2019-02-17 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogg', '0002_auto_20190216_2328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='content',
            new_name='Content',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='name',
            new_name='Name',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='Title',
            field=models.CharField(default='None', max_length=250),
        ),
    ]
