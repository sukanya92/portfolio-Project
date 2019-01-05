from django.db import models

#Create a blog models
#Title Pub_Date body Image
#Add the blog app to the settings
#Create a migration
#Migrate
#Add to the admin

class Blog(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    pub_Date = models.DateTimeField(null=True, blank=True)
    body = models.CharField(max_length=200,null=True, blank=True)
    image = models.ImageField(upload_to='images/',null=True, blank=True)

    #def __str__(self):
    #    return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_Date.strftime('%b %e %Y')
