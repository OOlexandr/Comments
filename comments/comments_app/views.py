from django.shortcuts import render, redirect
from comments_app.forms import CommentForm
from comments_app.models import Comment
from math import ceil

PAGE_SIZE = 2

def view_comment(request):
    order_by = request.GET.get("order_by") if request.GET.get("order_by") else "created"
    order = request.GET.get("order") if request.GET.get("order") != None else "-"
    page = int(request.GET.get("page")) if request.GET.get("page") else 0
    n_pages = ceil(Comment.objects.filter(parent__isnull=True).__len__() / PAGE_SIZE) - 1
    comments = Comment.objects.filter(parent__isnull=True).order_by(order + order_by)[page*PAGE_SIZE:(page+1)*PAGE_SIZE]
    form = CommentForm()
    print(order+order_by)
    return render(request, 'comments_app/view_comments.html', {'comments': comments, 'form': form, "order_by": order_by,
                                                               "order": order, "page": page, "n_pages": n_pages})

def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid() and request.POST.get("captcha") == request.POST.get("captcha_answer"):
            form.save()

    return redirect(to='comments_app:view_comments')