# Generated by Django 3.0.7 on 2020-08-01 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0005_showtime'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cinema',
            options={'verbose_name': 'سینما', 'verbose_name_plural': 'سینما'},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': 'فیلم', 'verbose_name_plural': 'فیلم'},
        ),
        migrations.AlterModelOptions(
            name='showtime',
            options={'verbose_name': 'سانس', 'verbose_name_plural': 'سانس'},
        ),
        migrations.AlterField(
            model_name='cinema',
            name='address',
            field=models.TextField(verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='capacity',
            field=models.IntegerField(verbose_name='ظرفیت'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='cinema_code',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='کد سینما'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='city',
            field=models.CharField(default='تهران', max_length=50, verbose_name='شهر'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='name',
            field=models.CharField(max_length=50, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='phone',
            field=models.CharField(max_length=20, null=True, verbose_name='تلفن'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(max_length=1000, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=50, verbose_name='کارگردان'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='lenght',
            field=models.IntegerField(verbose_name='مدت زمان'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=50, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(verbose_name='سال تولید'),
        ),
        migrations.AlterField(
            model_name='showtime',
            name='cinema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketing.Cinema', verbose_name='سینما'),
        ),
        migrations.AlterField(
            model_name='showtime',
            name='free_seats',
            field=models.IntegerField(verbose_name='صندلی های خالی'),
        ),
        migrations.AlterField(
            model_name='showtime',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketing.Movie', verbose_name='فیلم'),
        ),
        migrations.AlterField(
            model_name='showtime',
            name='price',
            field=models.IntegerField(verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='showtime',
            name='saleble_seats',
            field=models.IntegerField(verbose_name='صندلی های قابل فروش'),
        ),
        migrations.AlterField(
            model_name='showtime',
            name='start_time',
            field=models.DateField(verbose_name='زمان شروع'),
        ),
    ]
