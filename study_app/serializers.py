from rest_framework import serializers
from .models import User, Exam, Test, Question, UserTestResult, UserAnswer


# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = User
#         fields = '__all__'

#     def create(self, validated_data):
#         password = validated_data.pop('password')
#         user = super().create(validated_data)
#         user.set_password(password)
#         user.save()
#         return user

#     def validate(self, data):
#         email = data.get('email')
#         mobile = data.get('mobile')
#         if not email and not mobile:
#             raise serializers.ValidationError("Either email or mobile must be provided.")
#         if email and mobile:
#             raise serializers.ValidationError("Provide either email or mobile, not both.")
#         return data



# serializers.py
from rest_framework import serializers
from .models import User
from django.contrib.auth.models import Group, Permission

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    full_name = serializers.CharField(required=False, allow_blank=True)
    groups = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Group.objects.all(), required=False
    )
    user_permissions = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Permission.objects.all(), required=False
    )

    class Meta:
        model = User
        fields ='__all__'
        extra_kwargs = {
            'first_name': {'required': False, 'allow_blank': True},
            'last_name': {'required': False, 'allow_blank': True},
            'email': {'required': False},
            'mobile': {'required': False},
            # Add other fields as needed
        }

    def validate(self, data):
        email = data.get('email')
        mobile = data.get('mobile')

        # Check if email or mobile is provided
        if not email and not mobile:
            raise serializers.ValidationError("Either email or mobile must be provided.")
        if email and mobile:
            raise serializers.ValidationError("Provide either email or mobile, not both.")

        # Ensure either full_name is provided or both first_name and last_name
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        full_name = data.get('full_name')

        if full_name:
            if first_name or last_name:
                raise serializers.ValidationError(
                    "Provide either full_name or both first_name and last_name, not both."
                )
        else:
            if not (first_name and last_name):
                raise serializers.ValidationError(
                    "Provide both first_name and last_name, or provide full_name."
                )

        # Validate password and confirm_password
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password:
            if not confirm_password:
                raise serializers.ValidationError({"confirm_password": "Please confirm your password."})
            if password != confirm_password:
                raise serializers.ValidationError({"password": "Password and Confirm Password do not match."})

        return data
    

    def create(self, validated_data):
        password = validated_data.pop('password')
        groups = validated_data.pop('groups', [])
        user_permissions = validated_data.pop('user_permissions', [])

        # Handle full_name to first_name and last_name
        full_name = validated_data.pop('full_name', None)
        if full_name:
            names = full_name.strip().split(' ', 1)  # Split by first space
            validated_data['first_name'] = names[0]
            validated_data['last_name'] = names[1] if len(names) > 1 else ''

        # Create the user instance
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        # Assign many-to-many fields
        if groups:
            user.groups.set(groups)
        if user_permissions:
            user.user_permissions.set(user_permissions)

        # Update full_name based on first_name and last_name
        user.full_name = f"{user.first_name} {user.last_name}".strip()
        user.save()

        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        groups = validated_data.pop('groups', None)
        user_permissions = validated_data.pop('user_permissions', None)

        # Handle full_name to first_name and last_name
        full_name = validated_data.pop('full_name', None)
        if full_name:
            names = full_name.strip().split(' ', 1)
            instance.first_name = names[0]
            instance.last_name = names[1] if len(names) > 1 else ''
        else:
            # If full_name not provided, allow updating first_name and last_name individually
            first_name = validated_data.get('first_name', instance.first_name)
            last_name = validated_data.get('last_name', instance.last_name)
            instance.first_name = first_name
            instance.last_name = last_name

        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # Handle password change
        if password:
            instance.set_password(password)

        # Assign many-to-many fields
        if groups is not None:
            instance.groups.set(groups)
        if user_permissions is not None:
            instance.user_permissions.set(user_permissions)

        # Update full_name based on first_name and last_name
        instance.full_name = f"{instance.first_name} {instance.last_name}".strip()
        instance.save()

        return instance

    def to_representation(self, instance):
        """Customize the representation of the user."""
        representation = super().to_representation(instance)
        # Ensure full_name reflects the combined first_name and last_name
        representation['full_name'] = f"{instance.first_name} {instance.last_name}".strip()
        return representation

        

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class UserTestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTestResult
        fields = '__all__'

class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = '__all__'
