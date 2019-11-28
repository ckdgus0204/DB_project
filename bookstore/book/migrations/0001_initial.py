# Generated by Django 2.1.7 on 2019-11-28 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accumulate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accumulate_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_num', models.IntegerField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=200)),
                ('book_name', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('stock', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField()),
                ('book_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('c_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('coupon_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('discount_percent', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_word', models.CharField(max_length=200)),
                ('book_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Buyer')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_num', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supply_date', models.DateField()),
                ('book_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
                ('supplier_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Supplier')),
            ],
        ),
        migrations.AddField(
            model_name='buy',
            name='c_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Buyer'),
        ),
        migrations.AddField(
            model_name='accumulate',
            name='c_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Buyer'),
        ),
        migrations.AddField(
            model_name='accumulate',
            name='coupon_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Coupon'),
        ),
    ]
