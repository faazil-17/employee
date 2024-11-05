from django.shortcuts import render,redirect,get_object_or_404

from django.views.generic import View

from crm.forms import EmployeeForm,SignUpForm,SignInForm

from crm.models import Employee

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout
# Create your views here.

class EmployeeCreateView(View):

    template_name="employee_add.html"

    form_class=EmployeeForm
    


    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data,files=request.FILES)


        if form_instance.is_valid():

            form_instance.save()

            return redirect("employee-list")


        return render(request,self.template_name,{"form":form_instance}) 


class EmployeeListView(View):

    template_name=("employee_list.html")

    def get(self,request,*args,**kwargs):


        search_text=request.GET.get("filter")

        

        qs=Employee.objects.all()

        return render(request,self.template_name,{"data":qs})
    
class EmployeeDetailView(View):

    template_name="employee_detail.html"

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Employee.objects.get(id=id)

        return render(request,self.template_name,{"data":qs})
    

class EmployeeDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Employee.objects.get(id=id).delete()

        return redirect("employee-list")


class EmployeeUpdateView(View):

    template_name="employee_update.html"

    form_class=EmployeeForm

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        employee_object=get_object_or_404(Employee,id=id)

        form_instance=self.form_class(instance=employee_object)

        return  render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        employee_object=get_object_or_404(Employee,id=id)

        form_data=request.POST

        form_instance=self.form_class(form_data,files=request.FILES,instance=employee_object)

        if form_instance.is_valid():

        

            form_instance.save()

            return redirect("employee-list")
        
        return render(request,self.template_name,{"form":form_instance})


class SignUpView(View):

    template_name="register.html"

    form_class=SignUpForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            User.objects.create_user(**data)



            return redirect("register")
        
        return render(request,self.template_name,{"form":form_instance})


class SigninView(View):

    template_name="sign_in.html"  

    form_class=SignInForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class

        return render(request,self.template_name,{"form":form_instance})
    

    def post(self,request,*args,**kwargs):


        form_data=request.POST

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            uname=data.get("username")

            pwd=data.get("password")
            
            user_object=authenticate(request,username=uname,password=pwd)

            if user_object:

                login(request,user_object)

                return redirect("employee-list")
            
        return render(request,self.template_name,{"form":form_instance})
    

class SignOutView(View):

    def get(self,request,*args,**kwargs):

        logout(request)

        return redirect("signin")

