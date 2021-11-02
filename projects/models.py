from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    client = models.CharField(max_length=50)
    buildup_area = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    type = models.CharField(max_length=20, null=True, blank=True, choices=(('Architecture','Architecture'),('Interior','Interior')))

    def __str__(self):
        return self.name + ' | ' + self.location

    def images(self):
        return ProjectImages.objects.filter(project=self)

    def thumbnail(self):
        all = ProjectImages.objects.filter(project=self).order_by('-id')
        # if len(all)==0:
        #
        return all[0]

class ProjectImages(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images')

    def __str__(self):
        return self.project.name
