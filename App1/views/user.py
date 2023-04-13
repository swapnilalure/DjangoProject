import logging
import os

from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.db import transaction
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from App1.models.user import User
from App1.serializers.user import UserSerializer
from App1.utils.base_response import BaseResponse
from App1.utils.constants import USER_NOT_FOUND, INCORRECT_CREDENTIALS, AUTHENTICATED_SUCCESSFULLY, LOGOOUT
from App1.utils.util import Util

logger = logging.getLogger(__name__)


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)

    @transaction.atomic
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            message = "User register successfully"
            return BaseResponse.response_message("success", UserSerializer(user).data, message)
        except Exception as e:
            transaction.set_rollback(True)
            logger.error("RC : " + str(e))
            return Response(Util.get_error_message(self, error_msg=str(e)))


class LoginView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            email = request.data.get("email", "")
            password = request.data.get("password", "")
            user = User.objects.get(email=email, is_deleted=False)
            if user is None:
                return BaseResponse.response_message("error", USER_NOT_FOUND)

            if not user.check_password(password):
                return BaseResponse.response_message("error", INCORRECT_CREDENTIALS)

            login(request, user)

            return BaseResponse.response_message("success",  AUTHENTICATED_SUCCESSFULLY)
        except Exception as e:
            return BaseResponse.response_message("error", e)


class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get('refresh')
            token_obj = RefreshToken(refresh_token)
            token_obj.blacklist()
            access_token = request.auth
            # Database = BlackListedToken.objects.create(
            #     user=request.user.id,
            #     token=access_token)
            # Database.save()
            Data = "Token Blacklisted"
            return BaseResponse.response_message("success", Data, LOGOOUT)
        except Exception as e:
            print(str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST)
