from django.db import models

# Create your models here.


class User(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	mobile=models.CharField(max_length=50)
	ID = models.AutoField(primary_key=True)
	class Meta:
		db_table= 'User'
	def __str__ (self):
		return  self.name
	


class Task (models.Model):
	task_details=models.TextField(max_length=50)
	task_type = [
        ('Pending', 'Pending'),
        ('Done', 'Done'),
    ]
	task_type = models.CharField(max_length=10, choices=task_type, default='Pending')
	User=models.ForeignKey(User, on_delete=models.CASCADE)
	class Meta: 
		db_table= 'Task'
	def __str__ (self):
		return str(self.task_details)


