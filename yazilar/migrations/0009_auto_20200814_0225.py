# Generated by Django 3.0.7 on 2020-08-13 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yazilar', '0008_auto_20200814_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yazi',
            name='başlık',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
