from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class PostModel(models.Model):
    title=models.CharField(max_length=100)
    summary=models.CharField(max_length=100,blank=True,null=True)
    image_url=models.ImageField(default='default_blog.png',upload_to='Images')
    content=models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering= ('-date_created',)

    def comment_count(self): #count of comments
        return self.comment_set.all().count() #this is called reverse relationship becoz we creating this fun in POST model and in comment model post is fk

    def comments(self): #this is for showing comments
        return self.comment_set.all()

    def __str__(self) :
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel,on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content