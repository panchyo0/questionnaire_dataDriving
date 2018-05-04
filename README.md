# questionnaire_dataDriving
Django code for data driving Questionnaire web site that providing users with different questionnaire.  Admin can dynamically change each questionnaire's question and the number of questions.

## Environment: 
   - virtualenv
    
## Required Software:
   - python 2.7
   - Django 1.11.8

## Used Libraries:
   - Twitter Bootstrap 3
   - Jquery  3.3.1

## Instructions to run locally:
   ###### If has django 1.11.8  
   - Navigate to src folder by cd src
   - Run local server by python manage.py runserver
   ###### If want to use Virtual envirenment
   - install virtualenv by pip install virtualenv
   - virtualenv questionnaire_dataDriving
   - cd questionnaire_dataDriving
   - Under questionnaire_dataDriving folder, active virtual environment by source bin activate
   - Pip freeze to check all required software installed. Otherwise Install all required softwares
   - Navigate to src folder by cd src
   - Run local server by python manage.py runserver
    
## Instruction to use questionnaire:
   - Make sure local server is running at http://127.0.0.1:8000/.
   - Login with admin page at http://127.0.0.1:8000/admin/  with super user (username: admin, password:1234abcd).
   - Add a new questionnaire by click add button in Questionnaires.
   - Add new questions  by click add button in Questions.
   - Add questions to questionnaire by click add button in Questionnaire_ questions.
   - Back to Home page (http://127.0.0.1:8000/), all opened questionnaires will show in home page if current user is not staff or super user. Otherwise home page will show all exist questionnaires.
   - Click one questionnaire, it will show all related questions. User can submit this questionnaire once they answer all questions. Otherwise it will display a message to warn. Once successful submit, browser will alert a success message and redirect to home page.
