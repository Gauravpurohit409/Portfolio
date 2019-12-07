from django.db import models


#Create A Blog models
	#title
	#publication date 
	#body
	#image
class Blog(models.Model):
	Title = models.CharField(max_length = 20)
	pub_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to = 'images/')


#Add the Blog app to the settings
# Create a migration
#Migrate 
#Add to their admin