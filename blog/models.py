from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length = 200)
	pub_date = models.DateField(auto_now = FALSE,auto_now_add = FALSE)
	body = models.CharField(max_length = none)
	image = models.ImageField(upload_to ='images/')
# title
# pub_date
# body
# image

# Add the Blog app to the settings

# Migrate

# Add to the admin