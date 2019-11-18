from django.db import models
from django.contrib.auth.models import User

class constituency(models.Model):
	const_loc=models.CharField(max_length=30)
	def __str__(self):
		return (self.const_loc)




class Voter_id(models.Model):
	v_name=models.CharField(max_length=30)
	v_age=models.IntegerField()
	v_id=models.IntegerField(unique=True)
	v_address=models.CharField(max_length=300)
	v_sex=models.CharField(max_length=6)
	v_Dob=models.DateTimeField(null=True)
	c_CID=models.ForeignKey(constituency,related_name='constituency_ID',on_delete=models.CASCADE,)
	def __str__(self):
		return (self.v_name)
	


class Aadhar_card(models.Model):
	name=models.CharField(max_length=30)
	age=models.IntegerField()
	Year_of_birth=models.IntegerField()
	Aa_number_id=models.IntegerField(unique=True)
	sex=models.CharField(max_length=6)
	state=models.CharField(max_length=30)
	district=models.CharField(max_length=30)
	address=models.CharField(max_length=300)
	pincode=models.IntegerField()
	v_VID=models.ForeignKey(Voter_id, related_name='voter',on_delete=models.CASCADE,unique=True)
	voted=models.BooleanField(default=False)
	def __str__(self):
		return (self.name)
	
	

class contestent(models.Model):
	c_name=models.CharField(max_length=30)
	const_Id=models.ForeignKey(constituency, related_name='constituency_id', on_delete=models.CASCADE,)
	c_img=models.CharField(max_length=50)
	c_AID=models.ForeignKey(Aadhar_card,related_name='aadhar_number',on_delete=models.CASCADE,unique=True)
	votes=models.IntegerField(default=0)
	def __str__(self):
		return (self.c_name)



class E_officer(models.Model):
	e_oname=models.CharField(max_length=30,unique=True)
	e_password=models.CharField(max_length=13)
	e_cid=models.ForeignKey(constituency, related_name='constituencyID', on_delete=models.CASCADE,unique=True)
	def __str__(self):
		return (self.e_oname)

	
	
	
	
	
	

# Create your models here.











