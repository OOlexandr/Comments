from django.shortcuts import render, redirect
from comments_app.forms import CommentForm

def main(request):
    return render(request, 'comment_app/index.html')

def comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='comments_app:main')
        else:
            return render(request, 'comments_app/add_comment.html', {'form': form})

    return render(request, 'comments_app/add_comment.html', {'form': CommentForm()})