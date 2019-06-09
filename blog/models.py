from django.db import models
from django.utils.text import slugify


class Blog(models.Model):
	tag = models.CharField(max_length=50, default="Development")
	title = models.CharField(max_length=200)
	pub_date = models.DateField()
	body = models.TextField()
	image = models.ImageField(upload_to='images/')
	slug = models.SlugField(
		verbose_name="Slug",
		allow_unicode=True,
		unique=True,
		default='',
		editable=False,
	)

	def __str__(self):
		return self.title

	def summary(self):
		suffix = ""
		if len(self.body) > 97:
			suffix = "..."
		return self.body[:100] + suffix

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Blog, self).save(*args, **kwargs)
