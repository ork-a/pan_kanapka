# Generated by Django 2.2.1 on 2019-06-02 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='sandwiches/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('calories_per_portion', models.IntegerField(null=True)),
                ('portion_size_grams', models.IntegerField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sandwich',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('accessible', models.BooleanField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='sandwiches/images/')),
                ('ingredients', models.ManyToManyField(to='sandwiches.Ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sandwiches.IngredientGroup'),
        ),
    ]
