from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
class Class(models.Model):
    code = models.CharField(_("ClassCode"), max_length=10)
    subject = models.CharField(_("Subject"), max_length=25)
    teachername = models.CharField(_("TeacherName"), max_length=30) 
    
    class Meta:
        db_table = 'Class'  

