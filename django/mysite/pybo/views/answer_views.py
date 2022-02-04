from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ..models import Answer, Question
from ..forms import  AnswerForm

@login_required(login_url='common:login')
def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    #question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())

    # answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    # answer.save()
    #return redirect('pybo:detail', question_id=question.id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            # return redirect('pybo:detail', question_id=question.id)
            return redirect('{}#answer_{}'.format(resolve_url('pybo:detail', question_id=answer.question.id), answer.id))
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)  

    
@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    '''
    pybo answer modify
    '''
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, "You don't have permission to modify.")
        return redirect('pybo:detail', question_id=answer.question.id)

    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            # return redirect('pybo:detail', question_id = answer.question_id)
            return redirect('{}#answer_{}'.format(resolve_url('pybo:detail', question_id = answer.question_id),answer.id))
    else :
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form':form }
    return render(request, 'pybo/answer_form.html', context)

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    '''
    pybo answer delete
    '''
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, "You don't have permission to delete.")
        return redirect('pybo:detail', question_id=answer.question.id)
    else :
        answer.delete()

    return redirect('pybo:detail', question_id = answer.question.id)

