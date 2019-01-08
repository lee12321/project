from django.forms import ModelForm, ModelChoiceField
from company.models import Company, Province, City, CompanyType


class RegisterForm(ModelForm):
    class Meta:
        model = Company
        exclude = ['State_choices']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['province'] = ModelChoiceField(queryset=Province.objects.all(), required=False)
        self.fields['city'] = ModelChoiceField(queryset=City.objects.all(), required=False)
        self.fields['c_type'] = ModelChoiceField(queryset=CompanyType.objects.all(), required=False)
