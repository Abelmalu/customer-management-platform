# Generated by Django 4.2.8 on 2023-12-14 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_order_tags_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('I', 'Indoor'), ('O', 'Outdoor')], max_length=255, null=True),
        ),
    ]
