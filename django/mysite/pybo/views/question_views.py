
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ..models import  Question
from ..forms import QuestionForm, AnswerForm

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
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)  

    
@login_required(login_url='common:login')
def question_create(request):
    '''
    pybo question register
    '''
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        ## how to handle and what does it mean if is_valid() is False
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else :
        form = QuestionForm()
    context = {'form': form }
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    '''
    pybo question modify
    '''
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, "You don't have pemission to modify.")
        return redirect('pybo:detail', question_id=question.id)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.save()
            return redirect('pybo:detail', question_id = question.id)
    else :
        form = QuestionForm(instance=question)
    context = { 'form': form }       
    return render(request, 'pybo/question_form.html', context)

    
@login_required(login_url='common:login')
def question_delete(request, question_id):
    '''
    pybo question delete
    '''
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, "You don't have permission to delete.")
        return redirect('pybo:detail', question_id=question.id)

    question.delete()
    return redirect('pybo:index')
