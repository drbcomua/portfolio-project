# Generated by Django 2.1.4 on 2019-06-09 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.CharField(default='Development', max_length=50),
        ),
    ]