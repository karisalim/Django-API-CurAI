# from drf_yasg import openapi
# from drf_yasg.views import get_schema_view
# from rest_framework import permissions
# from django.contrib import admin
# from django.urls import path,include
# from rest_registration.api.views import reset_password , change_password # لو كان عندك View مخصص
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

# schema_view = get_schema_view(
#     openapi.Info(
#         title="My API",
#         default_version='v1',
#         description="Test API",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="mostafa.3mad.salah@gmail.com"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )
# urlpatterns = [
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
#              name='schema-swagger-ui'),
#     path('swagger.yaml/', schema_view.without_ui(cache_timeout=0), name='swagger-yaml'),

#     path('admin/', admin.site.urls),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     # path('api/', include('user_auth.urls',namespace='user_auth')),
#     path('', include('register_user.urls',namespace='register_user')),
#     path('',include('rating.urls',namespace='rating')),
#     path('reset-password/', reset_password, name='reset-password'),
#     path("api/auth/change-password/", change_password, name="change-password"),

# ]
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.contrib import admin
from django.urls import path, include
from rest_registration.api.views import (
    reset_password,
    change_password,
    register_email,
    verify_email,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# ✅ تهيئة Swagger لتوثيق الـ API
schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="Test API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mostafa.3mad.salah@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # ✅ توثيق API باستخدام Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger.yaml/', schema_view.without_ui(cache_timeout=0), name='swagger-yaml'),

    # ✅ مسارات تسجيل الدخول و JWT
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # ✅ تضمين التطبيقات الأخرى
    path('', include('register_user.urls', namespace='register_user')),
    path('', include('rating.urls', namespace='rating')),

    # ✅ **إضافة مسارات إعادة تعيين كلمة المرور وتغييرها**
    path("api/auth/reset-password/", reset_password, name="reset-password"),
    path("api/auth/change-password/", change_password, name="change-password"),

    # ✅ **إضافة مسارات تسجيل البريد الإلكتروني والتحقق منه**
    path("api/auth/register-email/", register_email, name="register-email"),
    path("api/auth/verify-email/", verify_email, name="verify-email"),
]
