from django.shortcuts import render, redirect
from comments_app.forms import CommentForm
from comments_app.models import Comment

def view_comment(request):
    print(request.GET)
    order_by = request.GET.get("order_by")
    page = request.GET.get("page") if request.GET.get("page") else 0
    if order_by:
        comments = Comment.objects.filter(parent__isnull=True).order_by(request.GET.get("order") + order_by)[page*25:(page+1)*25]
    else:
        comments = Comment.objects.filter(parent__isnull=True).order_by('-created')[page*25:(page+1)*25]
    form = CommentForm()
    return render(request, 'comments_app/view_comments.html', {'comments': comments, 'form': form})

def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='comments_app:view_comments')
        else:
            comments = Comment.objects.filter(parent__isnull=True)
            return render(request, 'comments_app/view_comment.html', {'comments': comments, 'form': form})

    comments = Comment.objects.filter(parent__isnull=True)
    return render(request, 'comments_app/view_comment.html', {'comments': comments, 'form': CommentForm()})