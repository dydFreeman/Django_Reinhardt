from django.db import models

class Subject(models.Model):
	name = models.CharField(max_length=50)
	surname = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	age = models.IntegerField()
	cv = models.FileField(upload_to='/etc/')

class Activity(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=50)
	
class Meeting(models.Model):
	subject = models.ForeignKey(Subject)
	activity = models.ForeignKey(Activity)
	date = models.DateTimeField('Meeting date')
	notes = models.CharField(max_length=100)
