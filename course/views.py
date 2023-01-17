from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages 

def catalog(request):
    courses = Course.objects.filter(public=True)
    
    context = {'courses': courses}
    return render(request, 'course/Catalog.html', context)

def course(request, slug):
    course = Course.objects.get(slug=slug)
    titles = CourseTitle.objects.filter(course=course.id)
    # tasks = 
    
    context = {'course': course, 'titles': titles}
    return render(request, 'course/CourseInfo.html', context)

def createCourse(request):
    tags = Tag.objects.all()
    courses = Course.objects.all()
    
    if request.method == 'POST':
        title = request.POST['title']
        slug = "-".join(title.lower().split(' '))
        user = request.user
        image = request.FILES.get('image', None)
        tag = request.POST.get('tag')
        about  = request.POST.get('about')
        whatAreUWillLearn = request.POST.get('WhatAreUWillLearn')
        level = request.POST.get('level')
        initialRequirements = request.POST.get('InitialRequirements')
        
        validated = True
            
        if len(about) < 4: #! VALIDATION
            validated = False
            messages.error(request, 'About must be at least 10 characters')
            
        if (tag == None ): #! Tag Doesn't Selected
            validated = False
            messages.error(request, 'Tag must be selected')
            
        if len(title) < 10: #! Title 
            validated = False
            messages.error(request, 'Title must be at least 4 characters')
                    
        for course in courses:
            if slug == course.slug: #! Slug
                validated = False
                messages.error(request, 'This article already exists')
                       
        if validated == True:
            tag = Tag.objects.get(id = tag)
                                            
            form = Course.objects.create( #! Create Course
                title = title,
                slug = slug,
                user = user,
                image = image,
                tags = tag,
                about = about,
                whatAreUWillLearn = whatAreUWillLearn,
                level = level,
                initialRequirements = initialRequirements,
                public = False,
            )
            print("Post Has Been Created")
        
            form.save()
            return redirect('profile/'+str(request.user.username)+'/courses')
        else:
            messages.error(request, 'This article already exists')
            print("Post doesn't create")            
            
    context = {'tags': tags}
    return render(request, 'course/create/CreateCourse.html', context)

def updateInfoPanel(request, slug):
    page = 'UpdateInfoPanel'
    course = Course.objects.get(slug=slug)
    courses = Course.objects.all()
    tags = Tag.objects.all()
    
    if request.method == 'POST':
        title = request.POST.get('title')
        
        courseImage = course.image 
        #if u don't choice image, we get last image or None
        
        if courseImage == '' or courseImage == ' ':
            courseImage = None
            
        image = request.FILES.get('image', courseImage)
        tagId = request.POST.get('tag')
        about = request.POST.get('about')
        WhatAreUWillLearn = request.POST.get('WhatAreUWillLearn')
        level = request.POST.get('level')
        initialRequirements = request.POST['InitialRequirements']
        public = request.POST.get('public')
        
        if public == 'on':
            public = True
        else: 
            public = False
            
        tag = Tag.objects.get(id = tagId) # GET TAG FOR UPDATE
        
        validated = True
            
        if len(about) < 10: #! VALIDATION
            validated = False
            messages.error(request, 'About must be at least 10 characters')
            
        if (tag == None ): #! Tag Doesn't Selected
            validated = False
            messages.error(request, 'Tag must be selected')
            
        if len(title) < 4: #! Title 
            validated = False
            messages.error(request, 'Title must be at least 4 characters')
            
        if len(WhatAreUWillLearn) < 10: 
            validated = False
            messages.error(request, 'WhatAreUWillLearn must be at least 10 characters')
            
                       
        if validated == True:
            if course.title != title:
                course.title = title
            if course.image != image:
                course.image = image
            if course.about != about:
                course.about = about
            if course.tags.id != tag.id:
                course.tags = tag
            if course.whatAreUWillLearn != WhatAreUWillLearn:
                course.whatAreUWillLearn = WhatAreUWillLearn
            if course.level != level:
                course.level = level
            if course.initialRequirements != initialRequirements:
                course.initialRequirements = initialRequirements
            if course.public != public:
                course.public = public
            
            course.save()
            return redirect('courses:course', course.slug)
    
    context = {
        'page': page, 
        'course': course, 
        'tags': tags
    }
    return render(request, 'course/panel/coursePanel.html',context)  

def TasksPanel(request, slug):
    page = 'TasksPanel'
    course = Course.objects.get(slug=slug)
    CourseTitles = CourseTitle.objects.filter(course=course)
    
    
    
    if request.method == 'POST':
        title = request.POST.get('title')
        
        if len(title) > 3:
            form = CourseTitle.objects.create(
                title=title,
                course=course,
                public = True,
                place = CourseTitles.count() + 1,
            )
            form.save()
            
            return redirect('/courses/'+str(course.slug)+'/tasks-panel')
    
    context = {'page': page, 'course': course, 'CourseTitles': CourseTitles} 
    return render(request, 'course/panel/coursePanel.html', context)

def createTask(request, slug):
    page = 'create_task'
    course = Course.objects.get(slug=slug)
    CourseTitles = CourseTitle.objects.filter(course =course)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        course_title = request.POST.get('course_title')
        tag = request.POST.get('tag')
        public = True
        
        
        validated = True
        
        if len(title) < 4:
            validated = False
            messages.error(request, 'Title must be at least 4 characters')
            
        if course_title == None or course_title == '':
            validated = False
            messages.error(request, 'Course Title is None')
            
        if course == None or course == '':
            validated = False
            messages.error(request, 'Course is None')

        if tag == None or tag == '':
            validated = False
            messages.error(request, 'Tag is None')
        
        if tag == 'text':
            body = request.POST.get('body')
            
            if validated:
                if request.method == 'POST':
                    form = CourseTask.objects.create(
                        course = course,
                        courseTitle = CourseTitle.objects.get(id=course_title),
                        title = title,
                        description = description,
                        body = body,
                        public = public
                    )
                    form.save()
                    return redirect('courses:tasks-panel', course.slug)
                
        elif tag == 'video':
            video = request.POST.get('video')
    
    context = {'page': page, 'course': course, 'CourseTitles': CourseTitles} 
    return render(request, 'course/panel/coursePanel.html', context)