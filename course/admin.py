from django.contrib import admin
from .models  import Course, CourseComment, CourseTitle, CourseTask, Tag


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'updated')
    
class CourseCommentAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'message')

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class CourseCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'user', 'message')

admin.site.register(Course, CourseAdmin)
admin.site.register(CourseTitle)
admin.site.register(CourseTask)
admin.site.register(Tag, TagAdmin)
admin.site.register(CourseComment, CourseCommentAdmin)