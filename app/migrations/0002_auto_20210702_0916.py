# Generated by Django 3.2.5 on 2021-07-02 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(upload_to='images/{self.title}'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(upload_to='images/{self.title}'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(upload_to='images/{self.title}'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image4',
            field=models.ImageField(upload_to='images/{self.title}'),
        ),
    ]
