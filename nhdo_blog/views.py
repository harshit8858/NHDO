from django.shortcuts import redirect, render
from django.contrib import auth
from .models import Blog, Comment
from .forms import BlogForm, Commentform
from django.db.models import Q


def blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            if request.user.is_authenticated():
                f = form.save(commit = False)
                f.user = request.user
                f.save()
            else:
                form.save()

            return redirect("blog")
    else:
        form = BlogForm()
        form1 = Commentform()
    n = Blog.objects.all()
    n1 = Comment.objects.all()  # comment ka funct alag se bana hai...below!
    nav4="active"
    return render(request, 'nhdo_blog/main.html', {'text':n, 'form':form, 'nav4':nav4, 'comment':n1})


def blog_delete(request,d):
    n = Blog.objects.get(id=d)
    n.delete()
    return redirect("blog")


def blog_edit(request,d):
    n = Blog.objects.get(id=d)
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES,instance=n)
        if form.is_valid():
            form.save()
            return redirect("blog")
    else:
        form = BlogForm(instance=n)
    nav4="active"
    return render(request, 'nhdo_blog/edit.html', {'form':form, 'nav4':nav4})


def blog_search(request):
    if request.method == 'POST':
        s = request.POST['search']
        if s:
            sa = Blog.objects.filter(Q(title__icontains=s)|Q(content__icontains=s)|Q(user__username__exact=s))
            if sa:
                return render(request, 'nhdo_blog/search.html', {'text': sa,'t':s})
            else:
                return render(request, 'nhdo_blog/notfound.html')
        else:
            return redirect("blog")


# def my_files(request):
#     n = Box.objects.all()
#     m = like.objects.all()
#     if request.method == "POST":
#         form = ChangeForm(request.POST)
#         print(form.errors)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Success")
#         else:
#             return HttpResponse("Not Valid")
#     else:
#         form = ChangeForm()
#     return render(request, 'my_files.html', {'l':m ,'t':n, 'fullname':request.user.username, 'form':form})


def blog_comment(request):
    box_id = request.POST["take_id"]
    print(box_id)
    box_obj = Blog.objects.get(id=box_id)        # for grabbing particular post's comments
    print(box_obj)
    if request.method == 'POST':
         form1 = Commentform(request.POST)
         if form1.is_valid():
            f1=form1.save(commit=False)
            f1.box=box_obj
            f1.user=request.user
            f1.save()
            return redirect('blog')
    else:
        form1 = Commentform()
    return render(request, 'nhdo_blog/main.html', {'form1':form1})
