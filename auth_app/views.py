from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from study_app.models import User
from .forms import PasswordChangeForm, PasswordResetForm, OTPVerificationForm
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework import status


User = get_user_model()
# Register view
@api_view(['POST'])
def register_view(request):
    email = request.data.get('email')
    mobile = request.data.get('mobile')
    password = request.data.get('password')
    first_name = request.data.get('first_name', '')
    last_name = request.data.get('last_name', '')
    dob = request.data.get('dob', None)
    address = request.data.get('address', '')

    if not email and not mobile:
        return Response({"error": "Email or Mobile number must be provided."}, status=status.HTTP_400_BAD_REQUEST)

    if not password:
        return Response({"error": "Password is required."}, status=status.HTTP_400_BAD_REQUEST)

    if mobile and len(mobile) < 10:
        return Response({"error": "Invalid mobile number."}, status=status.HTTP_400_BAD_REQUEST)

    # Check if email or mobile already exists in the User model
    if email and User.objects.filter(email=email).exists():
        return Response({"error": "Email already exists."}, status=status.HTTP_400_BAD_REQUEST)

    if mobile and User.objects.filter(mobile=mobile).exists():
        return Response({"error": "Mobile number already exists."}, status=status.HTTP_400_BAD_REQUEST)

    # Create the user with email or mobile
    try:
        user = User.objects.create_user(
            email=email,
            mobile=mobile,
            password=password,
            first_name=first_name,
            last_name=last_name,
            dob=dob,
            address=address
        )
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)

# Login View
@csrf_exempt
@api_view(['POST'])
def login_view(request):
    """
    Login a user using email or mobile number and password.
    """
    identifier = request.data.get('identifier')  # This can be either email or mobile
    password = request.data.get('password')

    if not identifier or not password:
        return Response({"error": "Both identifier (email/phone) and password are required."},
                        status=status.HTTP_400_BAD_REQUEST)

    # Try to find the user by email or mobile
    user = None
    if '@' in identifier:  # It's an email
        try:
            user = User.objects.get(email=identifier)
        except User.DoesNotExist:
            return Response({"error": "User with this email does not exist."}, status=status.HTTP_404_NOT_FOUND)
    else:  # It's a mobile number
        try:
            user = User.objects.get(mobile=identifier)
        except User.DoesNotExist:
            return Response({"error": "User with this mobile number does not exist."}, status=status.HTTP_404_NOT_FOUND)

    # Check if the password is correct
    if user and user.check_password(password):
        # Authentication successful
        return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
    else:
        # Authentication failed
        return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
    
    
# Logout View
@csrf_exempt
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({"message": "Logout successful"})
    return JsonResponse({"error": "POST method required"}, status=405)

# Password Change View
@login_required
@csrf_exempt
def password_change_view(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.POST, user=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keep the user logged in
            return JsonResponse({"message": "Password changed successfully"})
        else:
            return JsonResponse({"error": "Invalid data", "details": form.errors}, status=400)
    return JsonResponse({"error": "POST method required"}, status=405)

# Password Reset View with OTP
@csrf_exempt
def password_reset_view(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            otp = get_random_string(length=6, allowed_chars="1234567890")
            user = form.cleaned_data["user"]
            user.otp_code = otp  # Save OTP to user model
            user.save()
            send_mail("Your OTP", f"Your OTP is {otp}", "from@example.com", [user.email])
            return JsonResponse({"message": "OTP sent successfully"})
        else:
            return JsonResponse({"error": "Invalid data", "details": form.errors}, status=400)
    return JsonResponse({"error": "POST method required"}, status=405)

# OTP Verification View
@csrf_exempt
def verify_otp_view(request):
    if request.method == "POST":
        form = OTPVerificationForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data["otp"]
            user = form.cleaned_data["user"]
            if user.otp_code == otp:
                return JsonResponse({"message": "OTP verified successfully"})
            else:
                return JsonResponse({"error": "Invalid OTP"}, status=400)
        else:
            return JsonResponse({"error": "Invalid data", "details": form.errors}, status=400)
    return JsonResponse({"error": "POST method required"}, status=405)
