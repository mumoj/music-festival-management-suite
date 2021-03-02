from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_field


class UserAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        middle_name = data.get('middle_name')

        if middle_name:
            user_field(user, 'middle_name', middle_name)

        return super().save_user(request, user, form, commit=commit)
