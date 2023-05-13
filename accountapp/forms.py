from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __init__(self,*arge,**kwargs):
        super().__init__(*arge,**kwargs)

        self.fields['username'].disabled = True
