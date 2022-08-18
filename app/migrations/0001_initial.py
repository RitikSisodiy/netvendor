# Generated by Django 3.2.12 on 2022-08-18 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='scrapCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100, null=True)),
                ('prix_bas_maison', models.BigIntegerField(default=0)),
                ('prix_moyen_maison', models.BigIntegerField(default=0)),
                ('prix_haut_maison', models.BigIntegerField(default=0)),
                ('prix_bas_apparetement', models.BigIntegerField(default=0)),
                ('prix_moyen_apparetement', models.BigIntegerField(default=0)),
                ('prix_haut_apparetement', models.BigIntegerField(default=0)),
                ('depuis_2_ans_maisons', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_2_ans_appartements', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_1_an_maisons', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_1_an_appartements', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_6_mois_maisons', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_6_mois_appartements', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_3_mois_maisons', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_3_mois_appartements', models.CharField(default=None, max_length=100, null=True)),
                ('Maisons', models.CharField(default=None, max_length=100, null=True)),
                ('Appartements', models.CharField(default=None, max_length=100, null=True)),
                ('de_35m2', models.TextField(blank=True, null=True)),
                ('key_35m2_80m2', models.TextField(blank=True, null=True)),
                ('key_80m2_110m2', models.TextField(blank=True, null=True)),
                ('plus_de_150m2', models.TextField(blank=True, null=True)),
                ('key_1_piece', models.TextField(blank=True, null=True)),
                ('key_2_pieces', models.TextField(blank=True, null=True)),
                ('key_3_pieces', models.TextField(blank=True, null=True)),
                ('plus_4_pieces', models.TextField(blank=True, null=True)),
                ('volume', models.TextField(blank=True, null=True)),
                ('evolution', models.TextField(blank=True, null=True)),
                ('Repartition_selon_lage', models.TextField(blank=True, null=True)),
                ('Repartition_selon_lactivite_Hommes', models.TextField(blank=True, null=True)),
                ('Repartition_selon_lactivite_Femmes', models.TextField(blank=True, null=True)),
                ('Habitants', models.CharField(default=None, max_length=100, null=True)),
                ('Population', models.CharField(default=None, max_length=100, null=True)),
                ('Superficie', models.CharField(default=None, max_length=100, null=True)),
                ('Marie', models.CharField(default=None, max_length=100, null=True)),
                ('Logements', models.CharField(default=None, max_length=100, null=True)),
                ('price_table', models.TextField(blank=True, null=True)),
                ('region', models.CharField(default=None, max_length=100, null=True)),
                ('department', models.CharField(default=None, max_length=100, null=True)),
                ('city', models.CharField(default=None, max_length=100, null=True)),
                ('quarter', models.CharField(default=None, max_length=100, null=True)),
                ('street', models.CharField(default=None, max_length=100, null=True)),
                ('top_city', models.IntegerField(default=0, max_length=100)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price_chart', models.TextField(blank=True, null=True)),
                ('source', models.CharField(max_length=1000, unique=True)),
            ],
            options={
                'db_table': 'Update_barometer_city',
            },
        ),
        migrations.CreateModel(
            name='scrapData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100, null=True)),
                ('prix_bas_maison', models.BigIntegerField(default=0)),
                ('prix_moyen_maison', models.BigIntegerField(default=0)),
                ('prix_haut_maison', models.BigIntegerField(default=0)),
                ('prix_bas_apparetement', models.BigIntegerField(default=0)),
                ('prix_moyen_apparetement', models.BigIntegerField(default=0)),
                ('prix_haut_apparetement', models.BigIntegerField(default=0)),
                ('depuis_2_ans_maisons', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_2_ans_appartements', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_1_an_maisons', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_1_an_appartements', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_6_mois_maisons', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_6_mois_appartements', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_3_mois_maisons', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_3_mois_appartements', models.CharField(default=None, max_length=100, null=True)),
                ('Maisons', models.CharField(default=None, max_length=100, null=True)),
                ('Appartements', models.CharField(default=None, max_length=100, null=True)),
                ('de_35m2', models.TextField(blank=True, null=True)),
                ('key_35m2_80m2', models.TextField(blank=True, null=True)),
                ('key_80m2_110m2', models.TextField(blank=True, null=True)),
                ('plus_de_150m2', models.TextField(blank=True, null=True)),
                ('key_1_piece', models.TextField(blank=True, null=True)),
                ('key_2_pieces', models.TextField(blank=True, null=True)),
                ('key_3_pieces', models.TextField(blank=True, null=True)),
                ('plus_4_pieces', models.TextField(blank=True, null=True)),
                ('volume', models.TextField(blank=True, null=True)),
                ('evolution', models.TextField(blank=True, null=True)),
                ('Repartition_selon_lage', models.TextField(blank=True, null=True)),
                ('Repartition_selon_lactivite_Hommes', models.TextField(blank=True, null=True)),
                ('Repartition_selon_lactivite_Femmes', models.TextField(blank=True, null=True)),
                ('Habitants', models.CharField(default=None, max_length=100, null=True)),
                ('Population', models.CharField(default=None, max_length=100, null=True)),
                ('Superficie', models.CharField(default=None, max_length=100, null=True)),
                ('Marie', models.CharField(default=None, max_length=100, null=True)),
                ('Logements', models.CharField(default=None, max_length=100, null=True)),
                ('price_table', models.TextField(blank=True, null=True)),
                ('region', models.CharField(default=None, max_length=100, null=True)),
                ('department', models.CharField(default=None, max_length=100, null=True)),
                ('city', models.CharField(default=None, max_length=100, null=True)),
                ('quarter', models.CharField(default=None, max_length=100, null=True)),
                ('street', models.CharField(default=None, max_length=100, null=True)),
                ('top_city', models.IntegerField(default=0, max_length=100)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price_chart', models.TextField(blank=True, null=True)),
                ('source', models.CharField(max_length=1000, unique=True)),
            ],
            options={
                'db_table': 'Update_barometer_region',
            },
        ),
        migrations.CreateModel(
            name='scrapQuarters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100, null=True)),
                ('prix_bas_maison', models.BigIntegerField(default=0)),
                ('prix_moyen_maison', models.BigIntegerField(default=0)),
                ('prix_haut_maison', models.BigIntegerField(default=0)),
                ('prix_bas_apparetement', models.BigIntegerField(default=0)),
                ('prix_moyen_apparetement', models.BigIntegerField(default=0)),
                ('prix_haut_apparetement', models.BigIntegerField(default=0)),
                ('depuis_2_ans_maisons', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_2_ans_appartements', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_1_an_maisons', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_1_an_appartements', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_6_mois_maisons', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_6_mois_appartements', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_3_mois_maisons', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_3_mois_appartements', models.CharField(default=None, max_length=100, null=True)),
                ('Maisons', models.CharField(default=None, max_length=100, null=True)),
                ('Appartements', models.CharField(default=None, max_length=100, null=True)),
                ('de_35m2', models.TextField(blank=True, null=True)),
                ('key_35m2_80m2', models.TextField(blank=True, null=True)),
                ('key_80m2_110m2', models.TextField(blank=True, null=True)),
                ('plus_de_150m2', models.TextField(blank=True, null=True)),
                ('key_1_piece', models.TextField(blank=True, null=True)),
                ('key_2_pieces', models.TextField(blank=True, null=True)),
                ('key_3_pieces', models.TextField(blank=True, null=True)),
                ('plus_4_pieces', models.TextField(blank=True, null=True)),
                ('volume', models.TextField(blank=True, null=True)),
                ('evolution', models.TextField(blank=True, null=True)),
                ('Repartition_selon_lage', models.TextField(blank=True, null=True)),
                ('Repartition_selon_lactivite_Hommes', models.TextField(blank=True, null=True)),
                ('Repartition_selon_lactivite_Femmes', models.TextField(blank=True, null=True)),
                ('Habitants', models.CharField(default=None, max_length=100, null=True)),
                ('Population', models.CharField(default=None, max_length=100, null=True)),
                ('Superficie', models.CharField(default=None, max_length=100, null=True)),
                ('Marie', models.CharField(default=None, max_length=100, null=True)),
                ('Logements', models.CharField(default=None, max_length=100, null=True)),
                ('price_table', models.TextField(blank=True, null=True)),
                ('region', models.CharField(default=None, max_length=100, null=True)),
                ('department', models.CharField(default=None, max_length=100, null=True)),
                ('city', models.CharField(default=None, max_length=100, null=True)),
                ('quarter', models.CharField(default=None, max_length=100, null=True)),
                ('street', models.CharField(default=None, max_length=100, null=True)),
                ('top_city', models.IntegerField(default=0, max_length=100)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price_chart', models.TextField(blank=True, null=True)),
                ('source', models.CharField(max_length=1000, unique=True)),
                ('idCity', models.ForeignKey(db_column='idCity', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.scrapcity')),
            ],
            options={
                'db_table': 'Update_barometer_quarter',
            },
        ),
        migrations.CreateModel(
            name='scrapStreets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100, null=True)),
                ('prix_bas_maison', models.BigIntegerField(default=0)),
                ('prix_moyen_maison', models.BigIntegerField(default=0)),
                ('prix_haut_maison', models.BigIntegerField(default=0)),
                ('prix_bas_apparetement', models.BigIntegerField(default=0)),
                ('prix_moyen_apparetement', models.BigIntegerField(default=0)),
                ('prix_haut_apparetement', models.BigIntegerField(default=0)),
                ('depuis_2_ans_maisons', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_2_ans_appartements', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_1_an_maisons', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_1_an_appartements', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_6_mois_maisons', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_6_mois_appartements', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_3_mois_maisons', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_3_mois_appartements', models.CharField(default=None, max_length=100, null=True)),
                ('Maisons', models.CharField(default=None, max_length=100, null=True)),
                ('Appartements', models.CharField(default=None, max_length=100, null=True)),
                ('de_35m2', models.TextField(blank=True, null=True)),
                ('key_35m2_80m2', models.TextField(blank=True, null=True)),
                ('key_80m2_110m2', models.TextField(blank=True, null=True)),
                ('plus_de_150m2', models.TextField(blank=True, null=True)),
                ('key_1_piece', models.TextField(blank=True, null=True)),
                ('key_2_pieces', models.TextField(blank=True, null=True)),
                ('key_3_pieces', models.TextField(blank=True, null=True)),
                ('plus_4_pieces', models.TextField(blank=True, null=True)),
                ('volume', models.TextField(blank=True, null=True)),
                ('evolution', models.TextField(blank=True, null=True)),
                ('Repartition_selon_lage', models.TextField(blank=True, null=True)),
                ('Repartition_selon_lactivite_Hommes', models.TextField(blank=True, null=True)),
                ('Repartition_selon_lactivite_Femmes', models.TextField(blank=True, null=True)),
                ('Habitants', models.CharField(default=None, max_length=100, null=True)),
                ('Population', models.CharField(default=None, max_length=100, null=True)),
                ('Superficie', models.CharField(default=None, max_length=100, null=True)),
                ('Marie', models.CharField(default=None, max_length=100, null=True)),
                ('Logements', models.CharField(default=None, max_length=100, null=True)),
                ('price_table', models.TextField(blank=True, null=True)),
                ('region', models.CharField(default=None, max_length=100, null=True)),
                ('department', models.CharField(default=None, max_length=100, null=True)),
                ('city', models.CharField(default=None, max_length=100, null=True)),
                ('quarter', models.CharField(default=None, max_length=100, null=True)),
                ('street', models.CharField(default=None, max_length=100, null=True)),
                ('top_city', models.IntegerField(default=0, max_length=100)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price_chart', models.TextField(blank=True, null=True)),
                ('source', models.CharField(max_length=1000, unique=True)),
                ('idQuarter', models.ForeignKey(db_column='idQuarter', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.scrapquarters')),
            ],
            options={
                'db_table': 'Update_barometer_street',
            },
        ),
        migrations.CreateModel(
            name='scrapDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100, null=True)),
                ('prix_bas_maison', models.BigIntegerField(default=0)),
                ('prix_moyen_maison', models.BigIntegerField(default=0)),
                ('prix_haut_maison', models.BigIntegerField(default=0)),
                ('prix_bas_apparetement', models.BigIntegerField(default=0)),
                ('prix_moyen_apparetement', models.BigIntegerField(default=0)),
                ('prix_haut_apparetement', models.BigIntegerField(default=0)),
                ('depuis_2_ans_maisons', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_2_ans_appartements', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_1_an_maisons', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_1_an_appartements', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_6_mois_maisons', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_6_mois_appartements', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_3_mois_maisons', models.CharField(default=None, max_length=100, null=True)),
                ('depuis_3_mois_appartements', models.CharField(default=None, max_length=100, null=True)),
                ('Maisons', models.CharField(default=None, max_length=100, null=True)),
                ('Appartements', models.CharField(default=None, max_length=100, null=True)),
                ('de_35m2', models.TextField(blank=True, null=True)),
                ('key_35m2_80m2', models.TextField(blank=True, null=True)),
                ('key_80m2_110m2', models.TextField(blank=True, null=True)),
                ('plus_de_150m2', models.TextField(blank=True, null=True)),
                ('key_1_piece', models.TextField(blank=True, null=True)),
                ('key_2_pieces', models.TextField(blank=True, null=True)),
                ('key_3_pieces', models.TextField(blank=True, null=True)),
                ('plus_4_pieces', models.TextField(blank=True, null=True)),
                ('volume', models.TextField(blank=True, null=True)),
                ('evolution', models.TextField(blank=True, null=True)),
                ('Repartition_selon_lage', models.TextField(blank=True, null=True)),
                ('Repartition_selon_lactivite_Hommes', models.TextField(blank=True, null=True)),
                ('Repartition_selon_lactivite_Femmes', models.TextField(blank=True, null=True)),
                ('Habitants', models.CharField(default=None, max_length=100, null=True)),
                ('Population', models.CharField(default=None, max_length=100, null=True)),
                ('Superficie', models.CharField(default=None, max_length=100, null=True)),
                ('Marie', models.CharField(default=None, max_length=100, null=True)),
                ('Logements', models.CharField(default=None, max_length=100, null=True)),
                ('price_table', models.TextField(blank=True, null=True)),
                ('region', models.CharField(default=None, max_length=100, null=True)),
                ('department', models.CharField(default=None, max_length=100, null=True)),
                ('city', models.CharField(default=None, max_length=100, null=True)),
                ('quarter', models.CharField(default=None, max_length=100, null=True)),
                ('street', models.CharField(default=None, max_length=100, null=True)),
                ('top_city', models.IntegerField(default=0, max_length=100)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price_chart', models.TextField(blank=True, null=True)),
                ('source', models.CharField(max_length=1000, unique=True)),
                ('idregion', models.ForeignKey(db_column='idregion', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.scrapdata')),
            ],
            options={
                'db_table': 'Update_barometer_departement',
            },
        ),
        migrations.AddField(
            model_name='scrapcity',
            name='idDepartment',
            field=models.ForeignKey(db_column='idDepartment', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.scrapdepartment'),
        ),
    ]
