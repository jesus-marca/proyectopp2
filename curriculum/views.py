from urllib import request
from django.shortcuts import get_object_or_404, redirect, render 
from django.views.generic import (TemplateView, DetailView,
                                    ListView, CreateView,
                                    UpdateView,DeleteView,FormView,)
from app_users.forms import UserForm, UserProfileInfoForm

#usuarios
from app_users.models import UserProfileInfo, User
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from .models import Standard, Subject, Lesson, Comment, WorkingDays, TimeSlots,SlotSubject
from django.urls import reverse_lazy
from .forms import CommentForm,ReplyForm, LessonForm, SlotSubjectForm
from django.http import HttpResponseRedirect

# para enviar correo

from django.core.mail import EmailMessage
from django.template.loader import render_to_string



class StandardListView(ListView):
    context_object_name = 'standards'
    extra_context = {
        'slotsSubjectAll':SlotSubject.objects.all(),
        
        "usersAll":UserProfileInfo.objects.all(),
        "numeroNiveles":Standard.objects.all(),
        "numeroCursos":Subject.objects.all(),
        "numeroCapitulos":Lesson.objects.all(),
        "subjectsAll":SlotSubject.objects.all(),
        "numeroComentarios":Comment.objects.all(),
        
        #de prueba
        "subjectslot1":SlotSubject.objects.filter(standard=1),
        "subjectslot2":SlotSubject.objects.filter(standard=2),
        "subjectslot3":SlotSubject.objects.filter(standard=3),
        "subjectslot4":SlotSubject.objects.filter(standard=4),
        "subjectslot5":SlotSubject.objects.filter(standard=5),
        #--------------
        
        'cursos':Subject.objects.all(),
        'slots': TimeSlots.objects.all(),
        
        #de prueba
        'cursos1': Subject.objects.filter(standard=1),
        'cursos2': Subject.objects.filter(standard=2),
        'cursos3': Subject.objects.filter(standard=3),
        'cursos4': Subject.objects.filter(standard=4),
        'cursos5': Subject.objects.filter(standard=5),
        #-------------
        'lessonsAll':Lesson.objects.all(),
        
        #de prueba
        'lesson1':Lesson.objects.filter(Standard=1),
        'lesson2':Lesson.objects.filter(Standard=2),
        'lesson3':Lesson.objects.filter(Standard=3),
        'lesson4':Lesson.objects.filter(Standard=4),
        'lesson5':Lesson.objects.filter(Standard=5),
        #------------
    }
    model = Standard
    template_name = 'curriculum/standard_list_view.html'
 
class UsersListView(ListView):
    context_object_name = 'standards'
    extra_context = {
        "usersAll":UserProfileInfo.objects.all(),
    }
    model = Standard
    template_name = 'curriculum/user_list_view.html'
    
class SubjectListView(DetailView):
    context_object_name = 'standards'
    extra_context = {
        'slots': TimeSlots.objects.all()
    }
    model = Standard
    template_name = 'curriculum/subject_list_view.html'

class LessonListView(DetailView):
    context_object_name = 'subjects'
    model = Subject
    template_name = 'curriculum/lesson_list_view.html'

class LessonDetailView(DetailView, FormView):
    context_object_name = 'lessons'
    model = Lesson
    template_name = 'curriculum/lesson_detail_view.html'
    form_class = CommentForm
    second_form_class = ReplyForm
    
    extra_context={
        "usuarios":UserProfileInfo.objects.all(),
        "total_usuarios": User.objects.all()
        
    }
    def get_context_data(self, **kwargs):
        context = super(LessonDetailView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(request=self.request)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(request=self.request)
        # context['comments'] = Comment.objects.filter(id=self.object.id)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'form' in request.POST:
            form_class = self.get_form_class()
            form_name = 'form'
        else:
            form_class = self.second_form_class
            form_name = 'form2'

        form = self.get_form(form_class)
        # print("the form name is : ", form)
        # print("form name: ", form_name)
        # print("form_class:",form_class)

        if form_name=='form' and form.is_valid():
            print("comment form is returned")
            return self.form_valid(form)
        elif form_name=='form2' and form.is_valid():
            print("reply form is returned")
            return self.form2_valid(form)


    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.Standard
        subject = self.object.subject
        return reverse_lazy('curriculum:lesson_detail',kwargs={'standard':standard.slug,
                                                             'subject':subject.slug,
                                                             'slug':self.object.slug})
    def form_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm.lesson_name = self.object.comments.name
        fm.lesson_name_id = self.object.id
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

    def form2_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm.comment_name_id = self.request.POST.get('comment.id')
        fm.save()
        return HttpResponseRedirect(self.get_success_url())


class LessonCreateView(CreateView):
    # fields = ('lesson_id','name','position','image','video','ppt','Notes')
    form_class = LessonForm
    context_object_name = 'subject'
    model= Subject
    template_name = 'curriculum/lesson_create.html' 

    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.standard
  
  
        #regresar a la normalidad si no se puede
        # return reverse_lazy('curriculum:lesson_list',kwargs={'standard':standard.slug,
        #                                                      'slug':self.object.slug}) 
        return reverse_lazy('curriculum:lesson_detail', kwargs={'slug':self.slug, 'standard':self.Standard.slug,'subject':self.subject.slug})
 
 
    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.Standard = self.object.standard
        fm.subject = self.object 
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

class LessonUpdateView(UpdateView):
    fields = ('name','position','video','ppt','Notes')
    model= Lesson
    template_name = 'curriculum/lesson_update.html'
    context_object_name = 'lessons'
    

class LessonDeleteView(DeleteView):
    model= Lesson
    context_object_name = 'lessons'
    template_name = 'curriculum/lesson_delete.html'

    def get_success_url(self):
        print(self.object)
        standard = self.object.Standard
        subject = self.object.subject
        #return antes de optimizar
        # return reverse_lazy('curriculum:lesson_list',kwargs={'standard':standard.slug,'slug':subject.slug})
        return reverse_lazy('curriculum:standard_list')

class SlotSubjectListView(ListView):
    context_object_name = 'standards'
    extra_context = {
        "total":Standard.objects.all(),
        'slotsAll': TimeSlots.objects.all(),
        "usersAll":UserProfileInfo.objects.all(),
        "numeroNiveles":Standard.objects.all(),
        "numeroCursos":Subject.objects.all(),
        "numeroCapitulos":Lesson.objects.all(),
        "subjectsAll":SlotSubject.objects.all(),
        "numeroComentarios":Comment.objects.all(),
                
        'cursos':Subject.objects.all(),
        'slots': TimeSlots.objects.all(),
        
        'lessonsAll':Lesson.objects.all(),        
    }
    model = Standard
    template_name = 'curriculum/slot_list.html'
    
class SlotSubjectCreateView(CreateView):
    # fields = ('lesson_id','name','position','image','video','ppt','Notes')
    form_class =  SlotSubjectForm
    context_object_name = 'subject'
    model= Subject
    template_name = 'curriculum/slot_subject_create.html' 

    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.standard
  
        # return reverse_lazy('curriculum:slots_list', kwargs={'slug':self, 'standard':self.standard.slug,'subject':self.slot_subject.slug})
        #regresar a la normalidad si no se puede
        # return reverse_lazy('curriculum:lesson_list',kwargs={'standard':standard.slug,
        #                                                      'slug':self.object.slug}) 
        # return reverse_lazy('curriculum:slots_list', kwargs={'slug':self.slug, 'standard':self.Standard.slug,'subject':self.subject.slug})
        return reverse_lazy('curriculum:slots_list')
 
 
    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.standard = self.object.standard
        fm.slot_subject = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())



# def SlotUpdateView(request, slug):
    # slotsSubject = slotsSubject.objects.get(slot=slug)

    # hour_start = request.POST.get('hour_startInput')
    # hour_end = request.POST.get('hour_endInput')
    # day = request.POST.get('dayInput')
    # standard=request.POST.get('standarsInput')
    # subject=request.POST.get('subjectInput')
    
    # if request.method == 'POST':

    #     slotsSubject.standard = standard
    #     slotsSubject.slot_subject = subject
    #     slotsSubject.day = day
        
        
        # slotsSubject.slot = skill
        
        
        # slotsSubject.slot.start_time = hour_start
        # slotsSubject.slot.end_time  = hour_end
        # slotsSubject.save()
        
        # messages.success(request, 'User: ' + name +' ¡Edit Success!')
        
        
        # return reverse_lazy('curriculum:slots_list')
    # return render (request, "edit.html", {"slotsSubject": slotsSubject})
    
    
    # return reverse_lazy('curriculum:slots_list')


class SlotUpdateView(UpdateView):
    fields = ('day','slot')
    model= SlotSubject 
    template_name = 'curriculum/slot_update.html'
    context_object_name = 'slotSubjects'


# def user_update(request,user):
#     user2 = get_object_or_404(User, username = user)
#     user = get_object_or_404(UserProfileInfo, user = user2)
#     form = UserForm(initial={'username':user2.username,'first_name':user2.first_name,'last_name':user2.last_name, 'email':user2.email,})
#     form2 = UserProfileInfoForm(initial={'user_type':user.user_type,'profile_pic':user.profile_pic, 'bio':user.bio})
    
#     if request.method == "POST" :
#         form=UserForm(request.POST)
#         form2=UserProfileInfo(request.POST)
        
#     if form.is_valid() and form2.is_valid():
#         print('valido')
#         # user=UserProfileInfo()
        
#         user.user.username=form.cleaned_data['username']
#         user.user.first_name=form.cleaned_data['first_name']
#         user.user.last_name=form.cleaned_data['last_name']
#         user.user.email=form.cleaned_data['email']
#         user.user_type=form2.cleaned_data['user_type']
#         user.profile_pic=form2.cleaned_data['profile_pic']
#         user.bio=form2.cleaned_data['bio']
#         user.save()
#         return reverse_lazy('curriculum:user_list_view.html')
#     else:
#         print('invalid')
#     return reverse_lazy('curriculum:user_list_view.html')
    
        
# def user_update1(request,user1):      
#     if request.method == "POST":
#         user_form = UserForm(data=request.POST)
#         profile_form = UserProfileInfoForm(data=request.POST)

#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save()
#             # user.set_password(user.password)
#             user.save()

#             profile = profile_form.save(commit=False)
#             profile.user = user
#             profile.save()

#             registered = True
#         else:
#             print(user_form.errors, profile_form.errors)
#     else:
#         user_form = UserForm()
#         profile_form = UserProfileInfoForm()

#     return render(request, 'app_users/registration.html',
#                             {'registered':registered,
#                              'user_form':user_form,
#                              'profile_form':profile_form})

def user_update(request,id):
    userprofile = UserProfileInfo.objects.get(id= id)
    data = {
        
        'usuario':userprofile
    }
    return render(request,'curriculum/user_update.html',data)

def edit_user(request):
    id = int(request.POST['id'])
    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    bio = request.POST['bio']
    print(bio)
    # profile_pic=request.POST['profile_pic']
    userprofile = UserProfileInfo.objects.get(id = id)    
    # userprofile.user.username = username
    # print(userprofile.user.username)
    # userprofile.user.first_name = first_name
    # print(userprofile.user.first_name)
    # userprofile.user.last_name = last_name
    # print(userprofile.user.last_name)
    # userprofile.user.email = email
    # print(userprofile.user.email)
    # userprofile.bio = bio
    # print(userprofile.bio)
    
    us=User.objects.get(id=userprofile.user.id)
    us.username = username
    us.first_name = first_name
    us.last_name = last_name
    us.email = email
    us.save()
    userprofile.user=us
    userprofile.bio = bio
    userprofile.save()
    
    
    
    # if UserProfileInfo.objects.get(id = id).save(update_fields=['bio'],  force_update=True):
    #     print('se guardo')
    # else:
    #     print('no guardo')
    # userp = User.objects.get(id = userprofile.user.id)
    # print(userp)
    # print(userprofile.user.username)
    # id2=userprofile.user.id
    # userobject= User.objects.get(id =id2 )
    # userprofile.user.username = username
    # print(userprofile.user.username)
    
    # userp.first_name = first_name
    # userp.last_name = last_name
    # userp.email = email
   
    # userprofile.bio = bio
    # userprofile.user=userp
   
    # userp.delete()
    # if userp.save() :
    #     print('guardo')
    # else :
    #     print('no guardo')
    # userprofile.save()
 
    # userprofile.profile_pic=profile_pic
    # if userprofile.save(update_fields=['user','bio']) :
    #     print('se guardo')
    # else :
    #     print('no se guardo')
                       
    # return redirect('/')
    return render(request ,'curriculum/updattte.html')


