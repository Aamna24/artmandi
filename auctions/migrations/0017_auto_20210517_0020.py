# Generated by Django 3.1.7 on 2021-05-16 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auto_20210517_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bider',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auctions.bid'),
        ),
    ]