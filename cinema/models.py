from django.db import models

class Movie(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	year_release = models.DateField(null=True)
	poster = models.ImageField(upload_to="posters")
	genre = models.ManyToManyField('Genre')
	country = models.ManyToManyField('Country')
	director = models.ManyToManyField('Director')
	actor = models.ManyToManyField('Actor')

	def __unicode__(self):
		return self.title

class Genre(models.Model):
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Country(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Director(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)

class Actor(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)

class BlogPost(models.Model):
	id_post = models.IntegerField()
	body = models.TextField()
	username = models.CharField(max_length=100)
	time = models.DateTimeField()

	def __unicode__(self):
		return self.body

class Likes(models.Model):
	like = models.IntegerField()
	dislike = models.IntegerField()