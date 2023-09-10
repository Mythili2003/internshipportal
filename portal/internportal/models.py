from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class Internship_details(models.Model):
    name = models.CharField(max_length=100, unique=True)
    duration = models.CharField(max_length=50)
    vacancies = models.PositiveIntegerField()
    last_date_to_apply = models.DateField()
    internship_type = models.CharField(max_length=10)
    start_date = models.DateField()
    description=models.CharField(max_length=5000, default=name)
    responsibilities=models.TextField()  
    requirements=models.TextField()  
    skills=models.TextField()  
    perks_and_benefits=models.TextField()  

class Applicant(models.Model):
    firname = models.CharField(max_length=100)
    lasname = models.CharField(max_length=100)
    mobile_regex = RegexValidator(
        regex=r'^[0-9]{10}$',
        message="Mobile number must contain exactly 10 digits and in the range (0-9)."
    )
    mobile = models.CharField(validators=[mobile_regex], max_length=10)
    email = models.EmailField(unique=True)
    jobtitle = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    edu = models.CharField(max_length=200)
    exp = models.TextField(max_length=500)
    projects = models.TextField(max_length=500)
    train = models.TextField(max_length=500)
    loc = models.TextField(max_length=500)
    skills = models.TextField()
    lan = models.TextField()
    why_job = models.TextField()
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.firname + ' ' + self.lasname
    
class contactform(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$')])  
    email = models.EmailField()
    COURSE_CHOICES = [
        ('ds', 'Data Science'),
        ('es', 'Embedded Systems'),
    ]
    course = models.CharField(max_length=2, choices=COURSE_CHOICES)
    query = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
   

    