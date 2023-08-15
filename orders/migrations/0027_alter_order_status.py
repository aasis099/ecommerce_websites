# Generated by Django 3.2 on 2023-08-12 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0026_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('New', 'New')], default='New', max_length=10),
        ),
    ]
