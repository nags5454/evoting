from django.shortcuts import render,redirect
#from django.shortcuts import render
from django.http import HttpResponse
from .models import constituency,Voter_id,Aadhar_card,contestent,E_officer

def home0(request):
	usr_check=E_officer.objects.all()
	if request.method == 'POST':
		e_user_id = request.POST['e_user_id']
		e_pwd = request.POST['e_pwd']
		for usr in usr_check:
			if(usr.e_oname==e_user_id and usr.e_password==e_pwd):
				return render(request,"home.html",{"usr":usr})
		msg="Invalid OFFICER USER ID or PASSWORD..!"
		back='home0'
		return render(request,'error.html',{'msg':msg,'back':back})
	return render(request,'home0.html')

def home(request,pk):
	usr=E_officer.objects.filter(id=pk).first()
	return render(request,'home.html',{"usr":usr})



def vote(request,pk):
	usr=E_officer.objects.filter(id=pk).first()
	if request.method == 'POST':
		a_num = request.POST['a_num']
		
		temp=Aadhar_card.objects.filter(Aa_number_id=a_num).first()
		if temp == None :
			msg="Aadhar id is invalid..!"
			back='vote'
			return render(request,'error.html',{'msg':msg,'back':back,"usr":usr})
		elif temp.voted == True:
			msg="You have already voted..!"
			back='vote'
			return render(request,'error.html',{'msg':msg,'back':back,"usr":usr})
		else:
			return redirect("details",pk=temp.id,pku=usr.id)
	return render(request,'vote.html',{"usr":usr})


def details(request,pk,pku):
	usr=E_officer.objects.filter(id=pku).first()
	single_adhar=Aadhar_card.objects.filter(id=pk).first()
	temp_c_id=single_adhar.v_VID.c_CID
	contestents= contestent.objects.filter(const_Id=temp_c_id)
	return render(request,'details.html',{'single_adhar':single_adhar,'contestents':contestents,"usr":usr})

def cast(request,pkcn,pka,pku):
	usr=E_officer.objects.filter(id=pku).first()
	s_a=Aadhar_card.objects.filter(id=pka).first()
	s_c=contestent.objects.filter(id=pkcn).first()
	
	
		#s_a.v_VID.voted=True
	vote=contestent.objects.filter(id=pkcn).first().votes+1
	Aadhar_card.objects.filter(id=pka).update(voted=True)
	contestent.objects.filter(id=pkcn).update(votes=vote)

	msg="You have casted your vote succesfully..!"
	back='vote'
	return render(request,'cast.html',{'msg':msg,'back':back,"usr":usr})

def electrol(request,pk):
	nv=0
	e_a=E_officer.objects.filter(id=pk).first()
	contestents= contestent.objects.filter(const_Id=e_a.e_cid)
	for cn in contestents:
		nv=nv+cn.votes
	return render(request,'electrol.html',{"contestents":contestents,"e_a":e_a,"nv":nv})


# Create your views here.












