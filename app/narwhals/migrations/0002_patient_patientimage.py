# Generated by Django 2.2.6 on 2019-10-31 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('narwhals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.TextField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='narwhals.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='PatientImage',
            fields=[
                ('imageid', models.IntegerField(primary_key=True, serialize=False)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='narwhals.Patient')),
            ],
        ),
    ]