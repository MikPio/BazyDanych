# Generated by Django 3.0.2 on 2020-01-04 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200104_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='producer_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.Producer'),
        ),
    ]
