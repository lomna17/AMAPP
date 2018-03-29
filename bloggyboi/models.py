from django.db import models
from django.utils import timezone

class Post(models.Model):
    variables = (("Auth", "author"),("Title", "title"),("Text", "text"),("Created", "created_date"),
                 ("Published", "published_date"),("Num","number"))
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    number = models.FloatField(default = 0)
    field = models.CharField(choices = variables, max_length = 25, default = "")
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    def field(self):
        return self.field
    