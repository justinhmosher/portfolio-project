from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length = 200)
	pub_date = models.DateField(auto_now = False,auto_now_add = False)
	body = models.CharField(max_length = 30000)
	blog_image = models.ImageField(upload_to ='blog-images/')
# title
# pub_date
# body
# image

# Add the Blog app to the settings

# Migrate

# Add to the admin