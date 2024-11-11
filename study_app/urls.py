from django.urls import path
from . import views  # Import all views

urlpatterns = [
    # User URLs
    path('users/', views.UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:id>/', views.UserDetailView.as_view(), name='user-detail'),
    
    # Exam URLs
    path('exams/', views.ExamListCreateView.as_view(), name='exam-list-create'),
    path('exams/<int:id>/', views.ExamDetailView.as_view(), name='exam-detail'),
    
    # Test URLs
    path('tests/', views.TestListCreateView.as_view(), name='test-list-create'),
    path('tests/<int:id>/', views.TestDetailView.as_view(), name='test-detail'),
    
    # Question URLs
    path('questions/', views.QuestionListCreateView.as_view(), name='question-list-create'),
    path('questions/<int:id>/', views.QuestionDetailView.as_view(), name='question-detail'),
    
    # UserTestResult URLs
    path('user-test-results/', views.UserTestResultListCreateView.as_view(), name='user-test-result-list-create'),
    path('user-test-results/<int:id>/', views.UserTestResultDetailView.as_view(), name='user-test-result-detail'),
    
    # UserAnswer URLs
    path('user-answers/', views.UserAnswerListCreateView.as_view(), name='user-answer-list-create'),
    path('user-answers/<int:id>/', views.UserAnswerDetailView.as_view(), name='user-answer-detail'),
    
    # path('api/login/', views.LoginView.as_view(), name='login'),
    # path('api/logout/', views.LogoutView.as_view(), name='logout'),
    # path('api/change-password/', views.ChangePasswordView.as_view(), name='change_password'),
]
