# Generated by Django 5.0.7 on 2024-07-21 08:49

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='categories',
        ),
        migrations.CreateModel(
            name='PostPageBlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_pages', to='blog.blogcategory')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='blog.blogpage')),
            ],
            options={
                'unique_together': {('page', 'blog_category')},
            },
        ),
    ]
