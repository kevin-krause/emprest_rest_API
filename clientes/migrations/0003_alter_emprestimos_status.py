# Generated by Django 4.2.2 on 2023-06-22 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_emprestimos_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='status',
            field=models.CharField(default='pendente', max_length=50),
        ),
    ]
