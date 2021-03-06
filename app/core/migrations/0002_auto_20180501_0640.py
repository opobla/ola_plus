# Generated by Django 2.0.2 on 2018-05-01 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='highereducationinstitution',
            name='origin',
        ),
        migrations.AddField(
            model_name='learningopportunityspecification',
            name='academic_term',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='learningopportunityspecification',
            name='code',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='learningopportunityspecification',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='learningopportunityspecification',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organizationalunit',
            name='code',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='highereducationinstitution',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='highereducationinstitution',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='learningopportunityspecification',
            name='organizational_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='los', to='core.OrganizationalUnit'),
        ),
        migrations.AlterField(
            model_name='organizationalunit',
            name='higher_education_institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ounits', to='core.HigherEducationInstitution'),
        ),
        migrations.AlterField(
            model_name='organizationalunit',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ounits', to='core.OrganizationalUnit'),
        ),
        migrations.AlterUniqueTogether(
            name='learningopportunityspecification',
            unique_together={('organizational_unit', 'code')},
        ),
        migrations.DeleteModel(
            name='HigherEducationInstitutionOrigin',
        ),
    ]
