from django.db import models
from django.urls import reverse


from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.title
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE ,related_name='question')
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    liked=models.ManyToManyField(User,default=None,blank=True,related_name='liked')

    def num_likes(self):
        return self.liked.all().count()
    
LIKE_CHOICES=(('LIKE','LIKE'),('UNLIKE','UNLIKE'),)


class Like(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE,related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value=models.CharField(choices=LIKE_CHOICES,default='Like',max_length=10)
  
     