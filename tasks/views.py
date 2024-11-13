from django.shortcuts import redirect, get_object_or_404
from .models import Comment, Task

def add_comment(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        comment_content = request.POST.get('comment')
        Comment.objects.create(task=task, user=request.user, content=comment_content)
        return redirect('task_detail', task_id=task.id)  # Предполагается, что есть URL для деталей задачи

