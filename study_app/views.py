from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Exam, Test, Question, UserTestResult, UserAnswer
from .serializers import UserSerializer, ExamSerializer, TestSerializer, QuestionSerializer, UserTestResultSerializer, UserAnswerSerializer
from django.shortcuts import get_object_or_404

# User Views
class UserListCreateView(APIView):

    def get(self, request):
        users = User.objects.filter(is_deleted=False)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):

    def get(self, request, id):
        user = get_object_or_404(User, id=id, is_deleted=False)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        user = get_object_or_404(User, id=id, is_deleted=False)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        user = get_object_or_404(User, id=id)
        user.is_deleted = True
        user.save()
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# Exam Views
class ExamListCreateView(APIView):

    def get(self, request):
        exams = Exam.objects.filter(is_deleted=False)
        serializer = ExamSerializer(exams, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExamDetailView(APIView):

    def get(self, request, id):
        exam = get_object_or_404(Exam, id=id, is_deleted=False)
        serializer = ExamSerializer(exam)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        exam = get_object_or_404(Exam, id=id, is_deleted=False)
        serializer = ExamSerializer(exam, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        exam = get_object_or_404(Exam, id=id)
        exam.is_deleted = True
        exam.save()
        return Response({'message': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# Test Views
class TestListCreateView(APIView):

    def get(self, request):
        tests = Test.objects.filter(is_deleted=False)
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestDetailView(APIView):

    def get(self, request, id):
        test = get_object_or_404(Test, id=id, is_deleted=False)
        serializer = TestSerializer(test)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        test = get_object_or_404(Test, id=id, is_deleted=False)
        serializer = TestSerializer(test, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        test = get_object_or_404(Test, id=id)
        test.is_deleted = True
        test.save()
        return Response({'message': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# Question Views
class QuestionListCreateView(APIView):

    def get(self, request):
        questions = Question.objects.filter(is_deleted=False)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetailView(APIView):

    def get(self, request, id):
        question = get_object_or_404(Question, id=id, is_deleted=False)
        serializer = QuestionSerializer(question)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        question = get_object_or_404(Question, id=id, is_deleted=False)
        serializer = QuestionSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        question = get_object_or_404(Question, id=id)
        question.is_deleted = True
        question.save()
        return Response({'message': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# UserTestResult Views
class UserTestResultListCreateView(APIView):

    def get(self, request):
        results = UserTestResult.objects.filter(is_deleted=False)
        serializer = UserTestResultSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserTestResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserTestResultDetailView(APIView):

    def get(self, request, id):
        result = get_object_or_404(UserTestResult, id=id, is_deleted=False)
        serializer = UserTestResultSerializer(result)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        result = get_object_or_404(UserTestResult, id=id, is_deleted=False)
        serializer = UserTestResultSerializer(result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        result = get_object_or_404(UserTestResult, id=id)
        result.is_deleted = True
        result.save()
        return Response({'message': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# UserAnswer Views
class UserAnswerListCreateView(APIView):

    def get(self, request):
        answers = UserAnswer.objects.filter(is_deleted=False)
        serializer = UserAnswerSerializer(answers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserAnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAnswerDetailView(APIView):

    def get(self, request, id):
        answer = get_object_or_404(UserAnswer, id=id, is_deleted=False)
        serializer = UserAnswerSerializer(answer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        answer = get_object_or_404(UserAnswer, id=id, is_deleted=False)
        serializer = UserAnswerSerializer(answer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        answer = get_object_or_404(UserAnswer, id=id)
        answer.is_deleted = True
        answer.save()
        return Response({'message': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


