from collections import UserList
from datetime import date
import timeit
from django.db import models

# Create your models here.

class Medecine(models.Model):
    id_med=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    image=models.ImageField(upload_to='photo')
    
    email=models.CharField(max_length=50)
    adress=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    num_téle=models.IntegerField
    num_equipe=models.IntegerField
    spécialité=models.CharField(max_length=50)
    def set_password(self, raw_password):


        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
   
    

    



class Infermier(models.Model):
    id_infer=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=25)
    prenom=models.CharField(max_length=25)
    image=models.ImageField(upload_to='photo')
    
    email=models.CharField(max_length=50)
    adress=models.CharField(max_length=25)
    password=models.CharField(max_length=8)
    num_téle=models.IntegerField

   

class Patient(models.Model):
    num_pat=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    adress=models.CharField(max_length=50)
    password=models.CharField(max_length=8)
    def set_password(self, raw_password):


        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
     

class Rapport(models.Model):
    num_rap=models.IntegerField(primary_key=True)
    text=models.FileField(upload_to='photo')
    id_med=models.ForeignKey(Medecine,on_delete=models.CASCADE)
    id_infer=models.ForeignKey(Infermier,on_delete=models.CASCADE)
    num_pat=models.ForeignKey(Patient,on_delete=models.CASCADE)

class Dossier_medecale(models.Model):
    
    id_dossier_médical=models.IntegerField(primary_key=True)
    
    num_pat=models.ForeignKey(Patient,on_delete=models.CASCADE)
    id_med=models.ForeignKey(Medecine,on_delete=models.CASCADE)
    num_rap=models.ForeignKey(Rapport,on_delete=models.CASCADE) 



class Planing(models.Model):
    id_plan=models.IntegerField(primary_key=True)
    ref=models.ImageField(upload_to='photo')
    
    
    id_med=models.ForeignKey(Medecine,on_delete=models.CASCADE)
    id_infer=models.ForeignKey(Infermier,on_delete=models.CASCADE)
    

class Abcense(models.Model):
    num_abs=models.IntegerField(primary_key=True)
    date=models.DateField
    time=models.TimeField
   
    raison=models.CharField(max_length=500)
    id_med=models.ForeignKey(Medecine,on_delete=models.CASCADE)
    id_infer=models.ForeignKey(Infermier,on_delete=models.CASCADE)

class administrator(models.Model):
    id_admin=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    image=models.ImageField(upload_to='photo')
    
    email=models.CharField(max_length=50)
    adress=models.CharField(max_length=50)
    password=models.CharField(max_length=8)
    id_med=models.ForeignKey(Medecine,on_delete=models.CASCADE)
    id_infer=models.ForeignKey(Infermier,on_delete=models.CASCADE)
    num_pat=models.ForeignKey(Patient,on_delete=models.CASCADE)
    

class driver(models.Model):
    id_driver=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    image=models.ImageField(upload_to='photo')
    
    email=models.CharField(max_length=50)
    adress=models.CharField(max_length=50)
    password=models.CharField(max_length=8)



from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


class User(models.Model):

    name=models.CharField(max_length=255)
    
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    

    def set_password(self, raw_password):


        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
   





    

    



    

    