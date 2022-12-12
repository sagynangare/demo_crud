from django import forms

from .models import Question, Choice

import datetime

class QuestionForm(forms.ModelForm):

	question_text=forms.CharField(
		widget=forms.TextInput(attrs={'placeholder':"Enter Question: ",
										"class":'form-control'}))

	pub_date=forms.DateField(initial=datetime.date.today)

	class Meta:
		model=Question
		fields='__all__'  #['question_text',]
