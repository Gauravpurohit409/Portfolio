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

	def summary(self):
		return self.body[:100]

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')

	def __str__(self):
		return self.Title
#Add the Blog app to the settings
# Create a migration
#Migrate 
#Add to their admin