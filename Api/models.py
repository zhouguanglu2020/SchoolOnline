from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=50)
    passwd = models.CharField(max_length=100)

    def __str__(self):
        return "schoolonlinesusers: Users  %s " % self.name

    class Meta:
        app_label = "default"

class Book(models.Model):
    user = models.CharField(max_length=50)
    bookname = models.CharField(max_length=100)

    def __str__(self):
        return "schoolonlinecourse:%s: %s" % (self.user, self.bookname)

    class Meta:
        app_label = "course"

class Log(models.Model):
    logid = models.CharField(max_length=50)
    logneirong = models.CharField(max_length=100)

    def __str__(self):
        return "schoolonlinelog: %s: %s" % (self.logid, self.logneirong)

    class Meta:
        app_label = "log"