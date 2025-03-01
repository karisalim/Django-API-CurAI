from rest_framework_simplejwt.tokens import RefreshToken
from rest_registration.api.serializers import DefaultRegisterUserSerializer,DefaultLoginSerializer
from .models import CustomUser, Specialization
from rest_framework import serializers
from rating.models import DoctorReview
from django.contrib.auth.hashers import make_password  # أضف هذا السطر

# class CustomRegisterUserSerializer(serializers.ModelSerializer):
#     specialization = serializers.PrimaryKeyRelatedField(queryset=Specialization.objects.all(), required=False)
#     consultation_price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
#     location = serializers.CharField(max_length=255, required=False)

#     class Meta:
#         model = CustomUser
#         fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password', 'gender', 'age', 'role', 'specialization', 'consultation_price', 'location']
#         extra_kwargs = {
#             'password': {'write_only': True}  # إخفاء كلمة المرور في الـ output
#         }



#     def validate(self, attrs):
#         role = attrs.get('role')
#         if role == 'doctor':
#             if not attrs.get('specialization'):
#                 raise serializers.ValidationError("Specialization is required for doctors.")
#             if not attrs.get('consultation_price'):
#                 raise serializers.ValidationError("Consultation price is required for doctors.")
#             if not attrs.get('location'):
#                 raise serializers.ValidationError("Location is required for doctors.")
#         elif role == 'patient':
#             if 'specialization' in attrs:
#                 attrs.pop('specialization')
#             if 'consultation_price' in attrs:
#                 attrs.pop('consultation_price')
#             if 'location' in attrs:
#                 attrs.pop('location')

#         return attrs

#     # def create(self, validated_data):
#     #     specialization = validated_data.pop('specialization', None) if validated_data.get('role') == 'doctor' else None
#     #     user = super().create(validated_data)

#     #     if user.role == 'doctor':
#     #         user.is_approved = False
#     #     else:
#     #         user.is_approved = True

#     #     if specialization:
#     #         user.specialization = specialization

#     #     user.save()
#     #     return user
#     def create(self, validated_data):
#         # تشفير كلمة المرور قبل الحفظ
#         validated_data['password'] = make_password(validated_data.get('password'))
        
#         # استخراج التخصص (إن وجد) وحفظه بشكل منفصل
#         specialization = validated_data.pop('specialization', None)
        
#         # إنشاء المستخدم
#         user = CustomUser.objects.create(**validated_data)
        
#         # تعيين التخصص إذا كان المستخدم طبيبًا
#         if user.role == 'doctor' and specialization:
#             user.specialization = specialization
#             user.is_approved = False  # يحتاج إلى موافقة المسؤول
#         else:
#             user.is_approved = True  # تفعيل تلقائي للمرضى
        
#         user.save()
#         return user

#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         refresh = RefreshToken.for_user(instance)
#         data["specialization"] = instance.specialization.name if instance.specialization else None
#         data.pop('password', None)
#         return data
    
#     specialization = serializers.PrimaryKeyRelatedField(queryset=Specialization.objects.all(), required=False)
#     consultation_price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
#     location = serializers.CharField(max_length=255, required=False)

#     class Meta:
#         model = CustomUser  # تحديد النموذج المستخدم
#         fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password', 'gender', 'age', 'role', 'specialization', 'consultation_price', 'location']  # تحديد الحقول التي سيتم التعامل معها

#     # التحقق من تكرار البريد الإلكتروني فقط
#     def validate_email(self, value):
#         if CustomUser.objects.filter(email=value).exists():
#             raise serializers.ValidationError("A user with that email already exists.")
#         return value

#     def validate(self, attrs):
#         role = attrs.get('role')
#         if role == 'doctor':
#             if not attrs.get('specialization'):
#                 raise serializers.ValidationError("Specialization is required for doctors.")
#             if not attrs.get('consultation_price'):
#                 raise serializers.ValidationError("Consultation price is required for doctors.")
#             if not attrs.get('location'):
#                 raise serializers.ValidationError("Location is required for doctors.")
#         elif role == 'patient':
#             if 'specialization' in attrs:
#                 attrs.pop('specialization')
#             if 'consultation_price' in attrs:
#                 attrs.pop('consultation_price')
#             if 'location' in attrs:
#                 attrs.pop('location')

#         return attrs

#     def create(self, validated_data):
#         specialization = validated_data.pop('specialization', None) if validated_data.get('role') == 'doctor' else None
#         user = super().create(validated_data)

#         if user.role == 'doctor':
#             user.is_approved = False
#         else:
#             user.is_approved = True

#         if specialization:
#             user.specialization = specialization

#         user.save()
#         return user

# def to_representation(self, instance):
#         data = super().to_representation(instance)
#         refresh = RefreshToken.for_user(instance)
#         # data["role"] = getattr(instance, "role", None)
#         data["specialization"] = instance.specialization.name if instance.specialization else None
#         # data["consultation_price"] = instance.consultation_price
#         # data["location"] = instance.location
#         # data["is_approved"] = instance.is_approved
#         data.pop('password', None)

#         return data

class CustomRegisterUserSerializer(serializers.ModelSerializer):
    specialization = serializers.PrimaryKeyRelatedField(
        queryset=Specialization.objects.all(),
        required=False,
        allow_null=True
    )
    consultation_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        allow_null=True
    )
    location = serializers.CharField(
        max_length=255,
        required=False,
        allow_blank=True
    )

    class Meta:
        model = CustomUser
        fields = [
            'username', 'first_name', 'last_name', 'email', 
            'phone_number', 'password', 'gender', 'age', 'role', 
            'specialization', 'consultation_price', 'location'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("البريد الإلكتروني مسجل مسبقًا.")
        return value

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        specialization = validated_data.pop('specialization', None)
        user = super().create(validated_data)
        user.is_active = False  # سيُفعّل عبر البريد
        user.is_approved = (user.role == 'doctor')  # يحتاج موافقة إذا كان طبيبًا
        user.save()
        return user

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('password', None)
        if instance.role == 'doctor':
            data['specialization'] = instance.specialization.name if instance.specialization else None
        return data

#rate serializers
class DoctorReviewSerializer(serializers.ModelSerializer):
    patient_username = serializers.CharField(source='patient.username', read_only=True)
    rating = serializers.IntegerField()

    class Meta:
        model = DoctorReview
        fields = ['patient_username', 'rating', 'comment', 'created_at']
        ref_name = 'RegisterUserDoctorReviewSerializer'  # تحديد ref_name بشكل صريح

# show Specialization with doctor is_approved
class DoctorSerializer(serializers.ModelSerializer):
    reviews = DoctorReviewSerializer(source='doctor_reviews', many=True, read_only=True)  # إضافة التقييمات للطبيب
    specialization = serializers.CharField(source='specialization.name', read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'specialization', 'consultation_price', 'location', 'reviews']



class SpecializationListSerializer(serializers.ModelSerializer):
    doctor_count = serializers.SerializerMethodField()

    class Meta:
        model = Specialization
        fields = ['id', 'name', 'doctor_count']

    def get_doctor_count(self, obj):
        """إرجاع عدد الأطباء الموافق عليهم في هذا التخصص"""
        return CustomUser.objects.filter(specialization=obj, role='doctor', is_approved=True).count()

class SpecializationDetailSerializer(serializers.ModelSerializer):
    doctors = DoctorSerializer(source='customuser_set', many=True, read_only=True)

    class Meta:
        model = Specialization
        fields = ['id', 'name', 'doctors']
    def get_doctors(self, obj):
        """إرجاع قائمة الأطباء الموافق عليهم فقط داخل هذا التخصص"""
        approved_doctors = CustomUser.objects.filter(specialization=obj, role='doctor', is_approved=True)
        return DoctorSerializer(approved_doctors, many=True).data
