# Generated by Django 2.1.3 on 2018-11-26 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdfiles', '0003_auto_20181127_0220'),
    ]

    operations = [
        migrations.AddField(
            model_name='omefile',
            name='title',
            field=models.CharField(help_text='Kaydetmek için başlık giriniz:', max_length=100, null=True, verbose_name='Başlık giriniz: '),
        ),
    ]
