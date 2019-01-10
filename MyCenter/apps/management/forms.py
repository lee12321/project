from django import forms
from django.utils.translation import gettext_lazy as _


class PermissionModelMultipleChoiceField(forms.ModelMultipleChoiceField):

    def label_from_instance(self, obj):
        permissions_translated = [
            _(w).replace('Can', 'Pode').replace('add', 'adicionar').replace('change', 'alterar').replace('delete',
                                                                                                         'excluir').replace(
                'view', 'visualizar') for w in (obj.name).split()]
        return ' '.join(permissions_translated)
