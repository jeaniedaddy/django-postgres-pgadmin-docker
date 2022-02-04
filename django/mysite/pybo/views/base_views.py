from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, Count
from pybo.models import Question

# Create your views here.
def index(request):
    '''
    pybo list
    '''
    page = request.GET.get('page','1')
    kw= request.GET.get('kw','') #search keyword
    so= request.GET.get('so','') #sort order

    if so == 'recommend' : 
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter','-create_date')
        pass
    elif  so == 'popular' :
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer','-create_date')
        pass
    else :
        question_list = Question.objects.order_by('-create_date')
    
    # question_list = Question.objects.order_by('-create_date')

    if kw :
        question_list = question_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            Q(author__username__icontains = kw) |
            Q(answer__author__username__icontains=kw) 
        ).distinct()

    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page':page, 'kw':kw, 'so':so}
    return render(request, 'pybo/question_list.html',context)

def detail(request, question_id):
    '''
    pybo detail 
    '''
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'pybo/question_detail.html',context)
