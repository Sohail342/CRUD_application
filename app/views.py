from django.shortcuts import  redirect, render
from django.contrib import messages
from .models import Employee

# Create your views here.
def crud(request):
    details = Employee.objects.all()
    return render(request, 'crud.html', {"employees":details})


def edit(request, user_id):
    # Retrieve user object from the database
    user = Employee.objects.get(pk=user_id)
    
    if request.method == 'POST':
        # Get updated data from the form
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
        # Update user fields
        user.employee_name = fname
        user.employee_email = email
        user.employee_address = address
        user.employee_phone_no = phone
        
        # Save updated user object
        user.save()
        
        messages.success(request, "Detail successfully updated")
        
        return redirect('crud')
    
    return render(request, 'edit.html')


def add(request):
    if request.method == 'POST':
        
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        details = Employee(employee_name=fname, employee_email=email, employee_address=address, employee_phone_no=phone)
        details.save()
        messages.success(request, "Detail Sucessfully added")
        return redirect('crud')

    return render(request, 'add.html')


def delete(request, user_id):
    user = Employee.objects.get(pk=user_id)
    user.delete()
    return redirect("crud")
    