# Generated by Django 2.1.4 on 2019-06-09 22:45

from django.db import migrations, models
import django.utils.datetime_safe
from django.template.defaultfilters import slugify


def create_blog_slug(apps, schema_editor):
    # We can't import the Blog model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Blog = apps.get_model("blog", "Blog")
    for blog in Blog.objects.all():
        blog.slug = slugify(blog.title)
        blog.save()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_tag'),
    ]

    operations = [
        migrations.RunPython(create_blog_slug),
        # migrations.AddField(
        #     model_name='blog',
        #     name='slug',
        #     field=models.SlugField(allow_unicode=True, default=django.utils.slugify(title), unique=True,
        #                            verbose_name='Slug'),
        #     preserve_default=False,
        # ),
    ]