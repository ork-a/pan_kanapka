# Generated by Django 2.2 on 2019-05-06 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alergeny',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ale_Nazwa', models.TextField(null=True)),
                ('Ale_Ikona', models.BinaryField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kanapki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Kan_Cena', models.FloatField(null=True)),
                ('Kan_Archiwalny', models.IntegerField(null=True)),
                ('Kan_Ikona', models.BinaryField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skladniki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Skl_Grupa', models.IntegerField()),
                ('Skl_Nazwa', models.TextField(null=True)),
                ('Skl_Archiwalny', models.IntegerField(null=True)),
                ('Skl_Kcal', models.IntegerField(null=True)),
                ('Skl_GramNaPorcje', models.IntegerField(null=True)),
                ('Skl_Cena', models.IntegerField(null=True)),
                ('Skl_Ikona', models.BinaryField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SkladnikiAlergeny',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SklA_AleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bulka.Alergeny')),
                ('SklA_SklId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bulka.Skladniki')),
            ],
        ),
        migrations.CreateModel(
            name='KanapkiSkladniki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KaS_Ilosc', models.IntegerField(null=True)),
                ('KaS_KanId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bulka.Kanapki')),
                ('KaS_SklId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bulka.Skladniki')),
            ],
        ),
    ]
