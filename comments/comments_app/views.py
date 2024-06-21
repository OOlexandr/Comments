from django.shortcuts import render, redirect
from comments_app.forms import CommentForm
from comments_app.models import Comment

def view_comment(request):
    comments = Comment.objects.filter(parent__isnull=True)
    form = CommentForm()
    return render(request, 'comments_app/view_comments.html', {'comments': comments, 'form': form})

def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='comments_app:view_comments')
        else:
            return render(request, 'comments_app/add_comment.html', {'form': form})

    return render(request, 'comments_app/add_comment.html', {'form': CommentForm()})