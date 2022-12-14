# Generated by Django 4.0.6 on 2022-08-17 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientNutr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('unit', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='amount',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='ingredientinfo',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='ingredientinfo',
            name='ingredient_nutr',
            field=models.ManyToManyField(blank=True, null=True, to='app.ingredientnutr'),
        ),
    ]
