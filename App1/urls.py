from django.urls import path
from App1.views.student import StudentViews
from rest_framework.urlpatterns import format_suffix_patterns
from App1.views.user import LoginView, LogoutView, RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

api_routes = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),

    path('get_all_student/', StudentViews.as_view({'get': 'get_all_student'}), name="get_all_student"),
    path('get_student_by_id/', StudentViews.as_view({'post': 'get_student_by_id'}), name="get_student_by_id"),
    path('add_student/', StudentViews.as_view({'post': 'add_student'}), name="add_student"),
    path('update_student/', StudentViews.as_view({'put': 'update_student'}), name="update_student"),
    path('get_student_by_name/', StudentViews.as_view({'post': 'get_student_by_name'}), name="get_student_by_name"),
    path('delete_student/', StudentViews.as_view({'post': 'delete_student'}), name="delete_student"),

]

urlpatterns = format_suffix_patterns(api_routes)
