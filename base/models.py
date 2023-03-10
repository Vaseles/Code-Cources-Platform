from django.db import models
from django.contrib.auth.models import User
from course.models import Course, CourseTask

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scores = models.IntegerField(default=0)
    
    image = models.ImageField(upload_to='profiles', blank=True, null=True, default=None)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=168, blank=True)

    number = models.CharField(max_length=12, blank=True)
    twitter = models.CharField(max_length=1000, blank=True)
    github = models.CharField(max_length=1000, blank=True)
    telegram = models.CharField(max_length=1000, blank=True)
    website = models.URLField(blank=True)
    
    #! Courses
    courses  = models.ManyToManyField(Course, blank=True)
    tasks = models.ManyToManyField(CourseTask, blank=True)
    
    #! Likes & Bookmarks
    likeCourses = models.ManyToManyField(Course, blank=True, related_name='likeCourses',  default='')
    bookmarkCourses = models.ManyToManyField(Course, blank=True, related_name='bookmarkCourses', default='')
    likeArticle = models.ManyToManyField(Course, blank=True, related_name='likeArticle',  default='')
    bookmarkArticle = models.ManyToManyField(Course, blank=True, related_name='likeBookmark',  default='')
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choiceCourse = models.ForeignKey(Course, on_delete=models.CASCADE)
    lessons = models.ManyToManyField(CourseTask)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta: 
        ordering = ('updated_at', 'created_at', )
    
    def __str__(self):
        return '{} - {}'.form(self.user.username, self.course.title)