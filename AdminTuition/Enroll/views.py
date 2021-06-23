from django.shortcuts import render, HttpResponseRedirect,redirect, HttpResponse
from .forms import StudentRegistration
from .models import User



# Create your views here.
def add_show(request):

	if request.method == 'POST':
		fm = StudentRegistration(request.POST)
		if fm.is_valid():
			nm = fm.cleaned_data['name']
			em = fm.cleaned_data['email']
			pw = fm.cleaned_data['password']
			
			reg = User(name=nm, email=em, password=pw)
			reg.save()
			fm = StudentRegistration()

	else:
		fm = StudentRegistration()

	stud = User.objects.all()
	stud_cnt = stud.count()

	ct = request.session.get('count',0)
	newcount = ct + 1
	request.session['count'] = newcount
	


	return render(request,'Enroll/addAndShow.html', {'form':fm, 'stu':stud, 'stud_count':stud_cnt, 'counts':newcount})


	#this function will delete

#deletes data
def delete_data(request, id):
	if request.method == 'POST':
		pi = User.objects.get(pk=id)
		pi.delete()
		return HttpResponseRedirect('/')


#this function will update / edit
def update_data(request, id):
	if request.method == 'POST':
		pi = User.objects.get(pk=id)
		fm = StudentRegistration(request.POST, instance=pi)
		if fm.is_valid():
			fm.save()
	else:
		pi = User.objects.get(pk=id)
		fm = StudentRegistration(instance=pi)
	return render(request, 'Enroll/updateStudent.html', {'form':fm})


#views



#def cnt(request):
	