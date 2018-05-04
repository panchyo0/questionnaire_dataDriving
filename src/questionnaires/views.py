# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.shortcuts import render,get_object_or_404,redirect,get_list_or_404
from django.forms.formsets import formset_factory

from .models import Questionnaire, Questionnaire_Question
from .forms import AnswerForm

"""
query all opened questionnaires when current user is not staff or super user.
query all questionnaires when current user is staff or super user.
do pagination.
"""
def allQuestionnaires(request):
    title='Please chooose one questionnaire as start.'
    eachPage=3
    if not request.user.is_staff or not request.user.is_superuser:
        quearyset=Questionnaire.objects.filter(is_open=True).order_by("-start_date")
    else:
        quearyset=Questionnaire.objects.all().order_by("-start_date")
    paginator = Paginator(quearyset, eachPage)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts=paginator.page(1)
    except EmptyPage:
        contacts=paginator.page(paginator.num_pages)
    context={
        "title":title,
        "objects_list":contacts,
    }
    return render(request,"questionnaires.html",context)

"""
getting each question related to current questionnaire.
saving answers of questionnaire into database.
Zipping question list and Formset, render to detail.html.
"""
def getQuestionnaire(request,pk):
    obj=get_object_or_404(Questionnaire,Id=pk)
    questionnaire_question=get_list_or_404(Questionnaire_Question,questionnaire_id=pk)
    question_list=getQuestions(questionnaire_question)
    number_of_question=len(question_list)
    AnswerFormSet = formset_factory(AnswerForm,extra=number_of_question)
    if request.method == 'POST':
        formset = AnswerFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for i in range(len(formset)):
                if formset[i].is_valid():
                    try:
                        instance=formset[i].save(commit=False)
                        instance.question=question_list[i]
                        instance.save()
                    except Exception as e:
                        raise Http404
        return redirect("questionnaires:questionnaireList")
    else:
        formset = AnswerFormSet()
    rows=zip(question_list,formset)
    context={
        "objects":obj,
        'formset': formset,
        "rows":rows
    }
    return render(request,"detail.html",context)

"""
according the given question array, return a list with question
"""
def getQuestions(array):
    questionList=[]
    for i in range(len(array)):
        questionList.append(array[i].question_id)
    return questionList
