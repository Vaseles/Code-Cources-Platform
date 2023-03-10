from django.urls import path 
from . import views

app_name='courses'

urlpatterns = [
    #! COURSE 
    path('courses', views.catalog, name='catalog'),
    path('courses/<str:slug>', views.course, name='course'),
    path('courses/<str:slug>/tasks/<str:pk>', views.task,name='task'),
    
    path('create-course', views.createCourse, name='create-course'),
    
    #! PANEL FOR COURSES 
    path('courses/<str:slug>/tasks-panel', views.TasksPanel, name='tasks-panel'),
    path('courses/<str:slug>/update-info-panel', views.updateInfoPanel, name='update-info-panel'),
    path('courses/<str:slug>/create-task', views.createTask, name='create-task'),
    
    path('courses/<str:slug>/course-titles/<str:course_title_id>/update', views.updateTitle, name='course-titles-update'),
    path('courses/<str:slug>/course-tasks/<str:task_id>/update', views.updateTask, name='course-update-task'),
    
    path('courses/<str:slug>/course-titles/<str:title_id>/delete', views.deleteTitle, name='course-title-delete'),
    path('courses/<str:slug>/course-task/<str:task_id>/delete', views.deleteTask, name='course-task-delete'),
    
    path('courses/<str:slug>/comments', views.ProfileComments, name='profile-comments'),
    path('courses/<str:slug>/reviews', views.ProfileReviews, name='profile-reviews'),
    
    #! REVIEWS AND COMMENTS
    path('courses/<str:slug>/reviews/<str:id>', views.deleteReview, name='course-review-delete'),
    path('courses/<str:slug>/task/<str:pk>/comments/<str:comment_id>', views.courseTaskCommentDelete, name='course-task-comment-delete'),

]
