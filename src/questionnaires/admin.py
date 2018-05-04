from django.contrib import admin
from .models import Question,Answer,Questionnaire_Question,Questionnaire

#display Question in admin. search by create time. filter by question
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_id',
                    'question',
                    'create_at']
    list_filter = ["create_at"]
    search_fields = ["question"]
admin.site.register(Question, QuestionAdmin)

#display Answer in admin, search by question_id or answer. filter by question
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_id',
                    'question',
                    'answer']
    list_filter = ["question"]
    search_fields = ["question__question_id",
                     "answer"]
admin.site.register(Answer, AnswerAdmin)

#display Questionnaire in admin.
#search by question id, question or questionnaire description. filter by is_open or start_date,
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ['Id',
                    'name',
                    'description',
                    'start_date',
                    'get_question_members',
                    'is_open']
    list_filter = ["is_open","start_date"]
    search_fields = ["questionnaire_question__question_id__question_id",
                     "questionnaire_question__question_id__question",
                     "description"]
    #for each questionnaire, show related questions.
    def get_question_members(self,obj):
        return "\n".join([p.question for p in obj.question_members.all()])

admin.site.register(Questionnaire, QuestionnaireAdmin)

#Add question for questionnaire
class Questionnaire_QuestionAdmin(admin.ModelAdmin):
    list_display = ['questionnaire_id',
                    'question_id']
    list_filter = ["questionnaire_id"]
    search_fields = ["question_id__question_id",
                     "question_id__question"]
admin.site.register(Questionnaire_Question, Questionnaire_QuestionAdmin)
