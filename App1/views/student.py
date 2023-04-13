from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from App1.models.student import Student
from App1.serializers.student import StudentSerializer
from App1.utils.base_response import BaseResponse
from App1.utils.constants import RNF, RECORDS_FEACHED_SUCCESSFULLY, AMCS
from App1.utils.util import Util
from App1.views.pagination import PageNumberCustomPagination


class StudentViews(ViewSet):
    permission_classes = [permissions.AllowAny]


    def get_all_student(self, request):
        try:
            student = Student.objects.all()

            # Pagination
            pagination = PageNumberCustomPagination()
            querysets = pagination.paginate_queryset(student, request)

            serializer = StudentSerializer(querysets, many=True).data
            return BaseResponse.response_message("success", serializer, RECORDS_FEACHED_SUCCESSFULLY)
        except Exception as e:
            print(e)
            return Response(Util.get_error_message(self, error_msg=RNF))

    def get_student_by_id(self, request):
        try:
            queryset = Student.objects.all().filter(id=request.data['student_id'])
            print("queryset", queryset)
            serializer = StudentSerializer(queryset, many=True).data
            return Response({
                "status_code": "200",
                "message": "Record Fetched Successfully",
                "data": serializer
            })
            # return BaseResponse.response_message("Success", serializer, RECORDS_FEACHED_SUCCESSFULLY)

        except Exception as e:
            print(e)
            return Response(Util.get_error_message(self, error_msg=RNF))

    def add_student(self, request):
        queryset = Student.objects.create(
            name=request.data['name'],
            subject=request.data['subject'],
            # address=request.data['address'],
            number=request.data['number'],
        )
        queryset.save()
        return Util.get_created_message(self, message=AMCS)

    def update_student(self, request):
        queryset = Student.objects.create(
            name=request.get('name'),
            subject=request.get('subject'),
            address=request.get('address'),
            number=request.get('number'),
        )
        queryset.save()
        return Util.get_created_message(self, message=AMCS)

    def get_student_by_name(self, request):
        try:
            student = Student.objects.filter(name__icontains=request.data['student_name'])
            print('student', student)
            serializer = StudentSerializer(student, many=True).data
            return Response({
                "status_code": "200",
                "message": "Record deleted Successfully",
                "data": serializer
            })
            # return BaseResponse.response_message("Success", serializer, RECORDS_FEACHED_SUCCESSFULLY)
        except Exception as e:
            print(e)
            return Response(Util.get_error_message(self, error_msg=RNF))

    def delete_student(self, request):
        try:
            student = Student.objects.filter(id=request.data['student_id'])
            print('student', student)
            serializer = StudentSerializer(student, many=True).data
            return Response({
                "status_code": "200",
                "message": "Record deleted Successfully",
                "data": serializer
            })
            # return BaseResponse.response_message("Success", serializer, RECORDS_FEACHED_SUCCESSFULLY)
        except Exception as e:
            print(e)
            return Response(Util.get_error_message(self, error_msg=RNF))

