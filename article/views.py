from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import Articleform
from django.contrib import messages
from .models import Article,comment
from django.contrib.auth.decorators import login_required
# Create your views here.
def articles(request):

    keyword=request.GET.get("keyword")
    
    if keyword:
        articles=Article.objects.filter(title__contains =keyword)
        return render(request,"articles.html",{"articles":articles})
    articles=Article.objects.all()
    return render(request,"articles.html",{"articles":articles})
def index(request):
  
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")
@login_required(login_url="user:login")
def dashboard(request):
    articles =Article.objects.filter(author=request.user)
    context ={   "articles":articles   }

    return render(request,"dashboard.html",context)
@login_required(login_url="user:login")
def addarticle(request):
    form=Articleform(request.POST or None,request.FILES or None)
    if form.is_valid():
        article=form.save(commit=False)
        article.author=request.user
        article.save()
        messages.success(request,("Makale başarıyla güncellendi."))
        
        return redirect("index")
    return render(request,"addarticle.html",{"form":form})
def detail(request,id):
    #article =Article.objects.filter(id=id).first()
    article =get_object_or_404(Article,id=id)
    
    return render(request,"detail.html",{"article":article})

@login_required(login_url="user:login")
def updateArticle(request,id):
    article=get_object_or_404(Article,id=id)
    form=Articleform(request.POST or None , request.FILES or None,instance=article)
    if form.is_valid():
        article=form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale başarıyla güncellendi.")
        return redirect("article:dashboard")
    return render(request,"update.html",{"form":form})

@login_required(login_url="user:login")
def deleteArticle(request,id):
    article=get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request,("Makale başarıyla silinmiştir."))
    return redirect("article:dashboard") 

def addcomment(request,id):
    article=get_object_or_404(Article,id=id)
    if request.method=="POST":
        comment_author=request.POST.get("comment_author")
        comment_content=request.POST.get("comment_content")
        newcomment=comment(comment_author=comment_author,comment_content=comment_content)
        newcomment.article=article
        newcomment.save()
    return redirect("/articles/article/"+str(id))