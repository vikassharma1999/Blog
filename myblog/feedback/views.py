from django.shortcuts import render,redirect
from.import forms
from.models import FeedBack


# Create your views here.
def thanks(request,):
	data=FeedBack.objects.all()

	return render(request,'feedback/thanks.html',{'data':data})
def about(request):
	return render(request,'feedback/about.html')



def feed(request):
	if(request.method=='POST'):
		form=forms.GiveFeedback(request.POST,request.FILES)
		if(form.is_valid):
			form.save()
			return redirect('feedback:thanks')

	else:
		form=forms.GiveFeedback()
	return render(request,'feedback/feed.html',{'form':form})
