# Generated by Django 2.2.1 on 2019-05-26 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptosignals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='currency',
            field=models.ManyToManyField(related_name='users', to='cryptosignals.Currency'),
        ),
    ]
