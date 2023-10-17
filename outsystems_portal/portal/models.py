from django.db import models

# Create your models here.
class PORTAL_TBL(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TITLE = models.CharField(max_length=100)
    DESCRIPTION = models.CharField(max_length=1000)
    INSERT_USER_ID = models.CharField(max_length=10)
    INSERT_DATE = models.DateTimeField()
    UPDATE_USER_ID = models.CharField(max_length=10)
    UPDATE_DATE = models.DateTimeField()
         
    def __str__(self):
        return self.ID