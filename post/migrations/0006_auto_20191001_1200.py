# Generated by Django 2.0.10 on 2019-10-01 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20191001_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='post.Post'),
        ),
    ]
