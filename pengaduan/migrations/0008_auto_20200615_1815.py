# Generated by Django 3.0 on 2020-06-15 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pengaduan', '0007_aduan_status_aduan'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kampung',
            options={'ordering': ['id_kampung']},
        ),
        migrations.AddField(
            model_name='aduan',
            name='anonim',
            field=models.CharField(blank=True, default='tampil', max_length=20),
        ),
        migrations.AlterField(
            model_name='aduan',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='aduan',
            name='status_aduan',
            field=models.CharField(blank=True, default='Not Read', max_length=15),
        ),
        migrations.AlterField(
            model_name='kampung',
            name='distrik',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kampungs', to='pengaduan.Distrik'),
        ),
        migrations.AlterUniqueTogether(
            name='kampung',
            unique_together={('distrik', 'id_kampung')},
        ),
    ]