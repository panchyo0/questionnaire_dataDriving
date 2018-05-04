# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Questionnaire model.

#Question model.
class Question(models.Model):
    question_id=models.AutoField(primary_key=True)
    create_at=models.DateTimeField(auto_now_add=True,auto_now=False)
    question=models.CharField(max_length=5000,null=False,blank=False)
    def __str__(self):
        return self.question
    def __getitem__(self, key):
        return self

#questionnaire has ManyToMany relation with question.
class Questionnaire(models.Model):
    Id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=1024)
    description=models.CharField(max_length=5000)
    is_open=models.BooleanField(default=False)
    start_date=models.DateTimeField(auto_now_add=True,auto_now=False)
    question_members=models.ManyToManyField(Question,through='Questionnaire_Question')
    def __str__(self):
        return self.name

#related question and questionnaire according ID
class Questionnaire_Question(models.Model):
    questionnaire_id=models.ForeignKey(Questionnaire)
    question_id=models.ForeignKey(Question)

#answer model.
class Answer(models.Model):
    answer_id=models.AutoField(primary_key=True)
    question=models.ForeignKey(Question)
    answer=models.CharField(max_length=5000,null=False,blank=False)
    def __str__(self):
        return self.answer
