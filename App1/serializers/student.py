from rest_framework import serializers
from App1.models.student import Student


class StudentSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return obj.id

    class Meta:
        model = Student
        fields = ["id", "name", "subject", "address", "number"]
