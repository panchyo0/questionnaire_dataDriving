from django.conf.urls import url

from .views import(
        allQuestionnaires,
        getQuestionnaire,
        )
"""
URL rooter for questionnaire which include list all questionnaires, detail.
"""
urlpatterns = [
    #URL for all questionnaires
    url(r'^$',allQuestionnaires,name = "questionnaireList"),
    #URL for current questionnaire 
    url(r'^(?P<pk>\d+)/$',getQuestionnaire,name="detail"),
]
