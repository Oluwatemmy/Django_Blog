from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Employee, BlogPosts
from django.db.models import Q

# Create your views here.

def index(request):
    myEmployees = Employee.objects.all().order_by('name')
    template = loader.get_template('employee/index.html')
    context = {
        'myEmployees': myEmployees
    }
    return HttpResponse(template.render(context, request))

def create(request):
    template = loader.get_template('employee/create_page.html')
    return HttpResponse(template.render({}, request))

def createData(request):
    name = request.POST['name']
    title = request.POST['title']
    employee = Employee(name=name, title=title)
    employee.save()
    return HttpResponseRedirect(reverse('employee'))

def delete(request,id):
    deleteEmployee = Employee.objects.get(id=id)
    deleteEmployee.delete()
    return HttpResponseRedirect(reverse('employee'))

def update(request, id):
    update_employee = Employee.objects.get(id=id)
    template = loader.get_template('employee/update_page.html')
    context = {
        'Employee' : update_employee
    }
    return HttpResponse(template.render(context, request))

def updateData(request, id):
    update_employee = Employee.objects.get(id=id)
    update_employee.name = request.POST['name']
    update_employee.title = request.POST['title']
    update_employee.save()
    return HttpResponseRedirect(reverse('employee'))


def blog(request):
    myBlogPosts = BlogPosts.objects.all()
    featuredPost = BlogPosts.objects.filter(featured= True)
    template = loader.get_template('employee/blog.html')
    context = {
        'myBlogPosts': myBlogPosts,
        'featuredPost': featuredPost
    }
    
    return HttpResponse(template.render(context, request))

def detailsPage(request, id):
    detailsPost = BlogPosts.objects.get(id=id)
    template = loader.get_template('employee/detailsPage.html')
    context = {
        'post': detailsPost
    }
    return HttpResponse(template.render(context, request))