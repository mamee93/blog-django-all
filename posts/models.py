from tinymce import HTMLField
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Profile_img = models.ImageField(upload_to='Profile_img/')

class Gategory(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post',related_name='post_view', on_delete=models.CASCADE, blank=True,null=True)
    
    def __str__(self):
        return self.user.username

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    contents = models.TextField()
    post = models.ForeignKey('Post',related_name='comments', on_delete=models.CASCADE, blank=True,null=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=100)
    #overview = models.TextField()
    content = HTMLField(null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    #comment_count = models.IntegerField(default=0)
    #view_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='post/')
    categories = models.ManyToManyField(Gategory)
    featured = models.BooleanField(default=0)
    previous_post = models.ForeignKey('self',related_name='previous', on_delete=models.SET_NULL, blank=True,null=True)
    next_post = models.ForeignKey('self',related_name='next', on_delete=models.SET_NULL, blank=True,null=True)
    
    
    def __str__(self):
        return self.title
    
    def  get_absolute_url(self):
        return reverse('post-detail', kwargs={'id': self.id})

    
    def  get_update_url(self):
        return reverse('post-update', kwargs={'id': self.id})

    def  get_delete_url(self):
        return reverse('post-delete', kwargs={'id': self.id})

    
    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    @property
    def Comment(self):
        return PostView.objects.filter(post=self).count()

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()



    
