from rest_framework import serializers
from anti_fake.models import Counterfeit_prodect


class CounterfeitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counterfeit_prodect
        fields = ('name', 'type', 'company', 'standard', 'date', 'period', 'place', 'rpoch', 'site')
