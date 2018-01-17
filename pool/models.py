from django.db import models

# Create your models here.
# User Component - extend the built-in User model by creating a proxy model
	## User-selected team name
	## Email - username for login
	## Password - password for login
	## Point total
	## Paid status

# Teams Component	
	## College
	## Mascot
	## Seeding
	## Total wins 
	## Total points - calculated incrementally
	## Underdog wins
	## Underdog bonus
	
# User Selections - one-to-one link? https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
	## User - authorized user only - personalized data
	## Bracket name
	## Round 1 array - CHOICES
	## Round 2 array - CHOICES
	## Round 3 array - CHOICES
	## Round 4 array - CHOICES
	## Round 5 array - CHOICES
	## Round 6 array - CHOICES
	
