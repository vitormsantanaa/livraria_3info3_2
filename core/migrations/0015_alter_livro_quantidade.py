from django.db import migrations, models


def validar_quantidades(apps, schema_editor):
    Livro = apps.get_model('core', 'Livro')
    for livro in Livro.objects.all().iterator():
        valor = livro.quantidade
        if valor is None or str(valor).strip() == '':
            livro.quantidade = '0'
            livro.save(update_fields=['quantidade'])
            continue
        try:
            numero = int(valor)
        except (ValueError, TypeError):
            raise ValueError(f'Livro {livro.pk}: quantidade inválida ({valor!r}). Corrija antes da migração.')
        if numero < 0 or str(numero) != str(valor).strip():
            raise ValueError(f'Livro {livro.pk}: quantidade inválida ({valor!r}). Corrija antes da migração.')


class Migration(migrations.Migration):
    dependencies = [('core', '0014_compra_total')]

    operations = [
        migrations.RunPython(validar_quantidades, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='livro',
            name='quantidade',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
