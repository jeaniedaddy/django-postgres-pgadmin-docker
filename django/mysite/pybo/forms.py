from django import forms
from pybo.models import Answer, Question, Comment 


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question # use this model
        fields = ['subject', 'content'] # attributes of Question to be used in QuestionForm
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }
        labels={
            'subject': 'SUBJECT',
            'content': 'CONTENT',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [ 'content' ]
        labels = {
            'content': 'content',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': 'content',
        }