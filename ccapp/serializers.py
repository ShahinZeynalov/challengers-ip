from rest_framework import serializers
from sms_app.models import Student
from account_app.models import User
from dashboard_app.models import Badge

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = []

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = '__all__'

class StudentDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    badges  = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = '__all__'

    def get_badges(self,obj):
        return BadgeSerializer(obj.badges.all(),many=True).data
