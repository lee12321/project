from company.models import Company, CompanyType
from rest_framework import serializers


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('user_name', 'c_name', 'c_type',)
