# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from .models import Questionnaire,Question,Answer,Questionnaire_Question
from .views import getQuestions
from django.test import Client
from .forms import *
# Create your tests here.
class QuestionnairesTestCase(TestCase):
    """docstring forQuestionnairesTestCase."""
    def setUp(self):
        question=Question.objects.create(question_id="1",
                                         create_at="null" ,
                                        question="who are you")
        Answer.objects.create(answer_id="1",
                              question=question,
                              answer="Tom")
        questionnaire=Questionnaire.objects.create(Id="1",
                                                    name="test1",
                                                    description="test",
                                                    is_open="True",
                                                    start_date="null")
        Questionnaire_Question.objects.create(questionnaire_id=questionnaire,
                                              question_id=question)
    def test_answer_relation(self):
        answer=Answer.objects.get(answer_id="1")
        self.assertEqual(answer.question.question_id, 1)

    def test_questionnaire_relation(self):
        questionnaire=Questionnaire.objects.get(Id="1")
        questionnaire_question=Questionnaire_Question.objects.get(questionnaire_id=questionnaire.Id)
        self.assertEqual(questionnaire_question.question_id.question,"who are you")

    def test_form_valid(self):
        question=Question.objects.get(question_id="1")
        form=AnswerForm(data={'answer_id': '2', 'question':question,'answer':'Jack'})
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        question=Question.objects.get(question_id="1")
        form=AnswerForm(data={'answer_id': '', 'question':question,'answer':''})
        self.assertFalse(form.is_valid())

    def test_getQuestion(self):
        array=[]
        questionnaire=Questionnaire.objects.get(Id="1")
        question=Question.objects.get(question_id="1")
        questionnaire_question=Questionnaire_Question.objects.get(questionnaire_id=questionnaire.Id)
        array.append(questionnaire_question)
        question_list=getQuestions(array)
        self.assertEqual(question_list[0],question)

    def test_home_page(self):
        c=Client()
        questionnaire=Questionnaire.objects.get(Id="1")
        response=c.get(reverse('questionnaires:questionnaireList'))
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.context['objects_list'][0],questionnaire)
