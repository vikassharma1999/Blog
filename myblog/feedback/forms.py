from django import forms
from.import models
class GiveFeedback(forms.ModelForm):
	class Meta:
		model=models.FeedBack
		fields=['feed_back']
class TextMe(forms.ModelForm):
	class Meta:
		model=models.Text
		fields=['name','email','mob_no','query']