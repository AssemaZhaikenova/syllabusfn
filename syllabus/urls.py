from django.urls import path
from .views import *
from syllabus import views_auth

urlpatterns = [
    path('', home_view, name='home'),
    path('create/', create_syllabus_view, name='create_syllabus'),
    path('correspondence/<int:syllabus_id>/', correspondence, name='correspondence'),
    path('delete_learning_outcome/<int:syllabus_id>/<int:outcome_id>/', delete_learning_outcome, name='delete_learning_outcome'),
    path('thematic_plan/<int:syllabus_id>/', thematic_plan, name='thematic_plan'),
    path('delete_thematic_plan/<int:syllabus_id>/<int:plan_id>/', delete_thematic_plan, name='delete_thematic_plan'),
    path('evaluation_system/<int:syllabus_id>/', evaluation_system, name='evaluation_system'),
    path('delete_evaluation_system/<int:syllabus_id>/<int:system_id>/', delete_evaluation_system, name='delete_evaluation_system'),
    path('literature_list/<int:syllabus_id>/', literature_list, name='literature_list'),
    path('philosophy_and_policy/<int:syllabus_id>/', philosophy_and_policy, name='philosophy_and_policy'),
    path('register/', views_auth.registration, name='register'),
    path('login/', views_auth.login_view, name='login'),
    path('logout/', views_auth.logout_view, name='logout'),
    path('account/', account, name='account'),
    path('syllabus/', syllabus_list, name='syllabus_list'),
    path('syllabus/<int:syllabus_id>/', syllabus_detail_edit, name='syllabus_detail_edit'),
    path('syllabus/<int:syllabus_id>/delete/', delete_syllabus, name='delete_syllabus'),
    path('download-syllabus/<int:syllabus_id>/docx/', download_syllabus, {'format': 'docx'},
         name='download_syllabus_docx'),
    path('download-syllabus/<int:syllabus_id>/pdf/', download_syllabus, {'format': 'pdf'},
         name='download_syllabus_pdf'),
    path('delete_literature/<int:syllabus_id>/<int:literature_id>/', delete_literature, name='delete_literature'),
    path('success_syllabus_creation/<int:syllabus_id>/', success_syllabus_creation, name='success_syllabus_creation'),

]
