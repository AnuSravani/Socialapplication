from django.shortcuts import render,redirect
from socialweb.forms import RegistrationForm,LoginForm,UserProfileForm,PostForm
from django.views.generic import View,TemplateView,UpdateView,CreateView,ListView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from socialweb.models import Posts,UserProfile,Comments
from django.urls import reverse_lazy
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator

def signin_requried(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper
decs=[signin_requried,never_cache]
# Create your views here.
class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"signup.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            return render(request,"signup.html",{"form":form})
        
class Loginview(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"signin.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            print(uname,pwd)
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
               login(request,usr)
               return redirect("index")
            else:
                return render(request,"signin.html",{"form":form})
        else:
            return render(request,"signin.html",{"form":form})


@method_decorator(decs,name="dispatch")
  
class ProfileCreateView(View):
    def get(self,request,*args,**kwargs):
        form=UserProfileForm()
        return render(request,"profile-create.html",{"form":form}) 

    def post(self,request,*args,**kwargs):
        form=UserProfileForm(request.POST,files=request.FILES)
        if form.is_valid():
            usr=User.objects.get(username=request.user.username)
            form.instance.user=usr
            form.save()
            return redirect("index")
        else:
            return render(request,"profile-create.html",{"form":form})

# class UserProfileView(View):
#     def get(self,request,*args,**kwargs):
        
#         qs=UserProfile.objects.filter(user=request.user)
#         return render(request,"profile-view.html",{"profile":qs})
@method_decorator(decs,name="dispatch")
class IndexView(CreateView,ListView):
    model=Posts
    form_class=PostForm
    template_name="index.html"
    success_url=reverse_lazy("index")
    context_object_name="post"

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)

@method_decorator(decs,name="dispatch")

class ProfileDetailView(TemplateView):
    template_name="profile-detail.html"
    success_url=reverse_lazy("index")

@method_decorator(decs,name="dispatch")
class ProfileUpdateView(UpdateView):
    model=UserProfile
    form_class=UserProfileForm
    template_name="profile-edit.html"
    success_url=reverse_lazy("index")
    pk_url_kwarg="id"


@method_decorator(decs,name="dispatch")   
class PostAddView(CreateView,ListView):
    model=Posts
    form_class=PostForm
    template_name="index.html"
    success_url=reverse_lazy("index")
    context_object_name="post"

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
# class PostListView(View):
#     def get(self,request,*args,**kwargs):
#         qs=Posts.objects.all()
#         return render(request,"posts-list.html",{"form":qs})
    

@method_decorator(decs,name="dispatch")
class PostDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Posts.objects.get(id=id).delete()
        return redirect("index")
@method_decorator(decs,name="dispatch")

class LikeView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        li=Posts.objects.get(id=id)
        li.like.add(request.user)
        li.save()
        return redirect("index")
@method_decorator(decs,name="dispatch")    
class DislikeView(View):
      def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        li=Posts.objects.get(id=id)
        li.like.remove(request.user)
        li.save()
        return redirect("index") 
@method_decorator(decs,name="dispatch")   
class CommentAddView(View):
    def post(self,request,*args,**kwargs):
        pid=kwargs.get("id")
        pst=Posts.objects.get(id=pid)
        usr=request.user
        cmt=request.POST.get("comment")
        Comments.objects.create(user=usr,post=pst,comment=cmt)
        return redirect("index")
    
@method_decorator(decs,name="dispatch")
class CommentDeleteView(View):
    def get(self,*args,**kwargs):
        id=kwargs.get("pk")
        Comments.objects.get(id=id).delete()
        return redirect("index")
@method_decorator(decs,name="dispatch")   
class CommmentUpvoteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        cmt=Comments.objects.get(id=id)
        cmt.upvote.add(request.user)
        cmt.save()
        return redirect("index")
@method_decorator(decs,name="dispatch")
class CommentRemoveView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        cmt=Comments.objects.get(id=id)
        cmt.upvote.remove(request.user)
        cmt.save()
        return redirect("index")
@method_decorator(decs,name="dispatch")
class PostUpdateView(UpdateView):
    model=Posts
    form_class=PostForm
    template_name="post-edit.html"
    success_url=reverse_lazy("index")
    pk_url_kwarg="id"

@method_decorator(decs,name="dispatch")
class SignoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("index")
   