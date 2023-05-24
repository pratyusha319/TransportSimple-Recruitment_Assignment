from django import forms


from app.models import *
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={'password':forms.PasswordInput}

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'description']
        widgets={'description':forms.TextInput(attrs={'class':'form-control'})}

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['question','description']
        widgets={'address':forms.TextInput(attrs={'class':'form-control'})}