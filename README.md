# questionnaire_dataDriving
Django code for data driving Questionnaire web site that providing users with different questionnaire.  Admin can dynamically change each questionnaire's question and the number of questions.

## Environment: 
   - virtualenv
    
## Required Software:
   - python 2.7</li>
   - Django 1.11.8</li>

## Used Libraries:
    <li>Twitter Bootstrap 3
    <li>Jquery  3.3.1

## Instructions to run locally:
   ###### if has django 1.11.8  
    <li>Navigate to src folder by cd src</li>
    <li>Run local server by python manage.py runserver</li>
   ###### if want to use Virtual envirenment
    <li>install virtualenv by pip install virtualenv</li>
    <li>virtualenv questionnaire_dataDriving</li>
    <li>cd questionnaire_dataDriving</li>
    <li>Under questionnaire_dataDriving folder, active virtual environment by source bin activate</li>
    <li>Pip freeze to check all required software installed. Otherwise Install all required softwares</li>
    <li>Navigate to src folder by cd src</li>
    <li>Run local server by python manage.py runserver</li>
    
## Instruction to use questionnaire:
    <li>Make sure local server is running at http://127.0.0.1:8000/</li>
    <li>Staring with admin page at http://127.0.0.1:8000/admin/  with super user (username: admin, password:1234abcd)</li>
    <li>Add a new questionnaire by click add button in Questionnaires</li>
    <li>Add new questions  by click add button in Questions</li>
    <li>Add questions to questionnaire by click add button in Questionnaire_ questions</li>
    <li>Back to Home page (http://127.0.0.1:8000/), all opened questionnaires will show in home page if current user is not staff or super user. Otherwise home page will show all exist questionnaires.</li>
    <li>Click one questionnaire, it will show all related questions. User can submit this questionnaire once they answer all questions. Otherwise it will display a message to warn. Once successful submit, browser will alert a success message and redirect to home page.</li>
