# crm_app/views.py
from django.shortcuts import render, get_object_or_404,redirect
from .forms import CarForm,CustomerForm,TransactionForm,UpdateTransactionForm,LeasingForm,UpdateLeasingForm
from django.http import JsonResponse
from .models import Cars,Customer,Transaction,Leasing
from django.contrib.auth.decorators import login_required



@login_required
def dashboard(request):
    return render(request, 'crm/dashboard.html')



# customers view
@login_required
def customer_details(request):
    customers = Customer.objects.all()
    context = {'customers': customers}

    return render(request, 'crm/customer/customer_details.html', context)



@login_required
def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crm:customer_details')
    else:
        form = CustomerForm()

    return render(request, 'crm/customer/add_customer.html', {'form': form})


def update_customer(request, user_id):
    customer = get_object_or_404(Customer, id=user_id)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('crm:customer_details')
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'crm/customer/customer_update_form.html', {'form': form, 'customer': customer})




def delete_customer(request, user_id):
    customer = get_object_or_404(Customer, id=user_id)

    if request.method == 'DELETE':
        customer.delete()
        return JsonResponse({'message': 'Customer deleted successfully'}, status=200)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)


# cars view  
def get_car_details(request):
    if request.method == 'GET':
        car_id = request.GET.get('id')
        try:
            car = Cars.objects.get(id=car_id)
            car_details = {
                'model': car.model,
                'year': car.year,
                'color': car.color,
                'engine': car.engine,
                'total_available_number': car.total_available_number,
                'is_still_in_stock': car.is_still_in_stock
            }
            return JsonResponse(car_details)
        except Cars.DoesNotExist:
            return JsonResponse({'error': 'Car not found.'}, status=404)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)




@login_required
def show_all_cars(request):
    cars = Cars.objects.all()
    context = {'cars': cars}
    return render(request, 'crm/cars/cars_dashboard.html', context)

@login_required
def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crm:show_all_cars')
    else:
        form = CarForm()

    return render(request, 'crm/cars/add_car.html', {'form': form})

@login_required
def update_car(request, car_id):
    car = get_object_or_404(Cars, id=car_id)

    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('crm:show_all_cars')
    else:
        form = CarForm(instance=car)

    return render(request, 'crm/cars/car_update_form.html', {'form': form, 'car': car})


# @login_required(login_url='/') #redirect when user is not logged in
@login_required
def delete_car(request, car_id):
    car = get_object_or_404(Cars, id=car_id)

    if request.method == 'DELETE':
        car.delete()
        return JsonResponse({'message': 'Car deleted successfully'}, status=200)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)



# transactions view

@login_required
def transaction_list(request):
    transactions = Transaction.objects.all()
    context = {'transactions': transactions}
    return render(request, 'crm/sell/transaction_list.html', context)


@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crm:transaction_list')
        else:
            # Form is not valid, handle the errors
            print("Form errors:", form.errors)
    else:
        form = TransactionForm()

    return render(request, 'crm/sell/sell_a_car.html', {'transaction_form': form})


def sold(request):
    if request.method == 'POST':
        car_id = request.POST.get('id')
        number_of_sold_str = request.POST.get('number_of_sold')

        # Check if number_of_sold_str is not empty and contains only digits
        if number_of_sold_str and number_of_sold_str.isdigit():
            number_of_sold = int(number_of_sold_str)
            
        else:
            return JsonResponse({"error": "Invalid number_of_sold value. Must be a positive integer."}, safe=False, status=400)

        try:
            car = Cars.objects.get(id=car_id)
            car.sold(number_of_sold)
            return JsonResponse({"message": "Car sold successfully."}, safe=False)
        except Cars.DoesNotExist:
            return JsonResponse({"error": "Car not found."}, safe=False, status=404)
        except ValueError as ve:
            return JsonResponse({"error": str(ve)}, safe=False, status=400)

    return JsonResponse({"error": "Invalid request method."}, safe=False, status=400)




def update_transaction(request,transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)

    if request.method == 'POST':
        form = UpdateTransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('crm:transaction_list')
    else:
        form = UpdateTransactionForm(instance=transaction)

    return render(request, 'crm/sell/transaction_update_form.html', {'form': form, 'transaction': transaction})


@login_required
def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    if request.method == 'DELETE':
        transaction.delete()
        return JsonResponse({'message': 'Transaction deleted successfully'}, status=200)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)



# leas view
@login_required
def leasing_list(request):
    leases = Leasing.objects.all()
    context = {'leases': leases}
    return render(request, 'crm/lease/leasing_list.html', context)


@login_required
def add_lease(request):
    if request.method == 'POST':
        form = LeasingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crm:leasing_list')
    else:
        form = LeasingForm()

    return render(request, 'crm/lease/lease_a_car.html', {'lease_form': form})



@login_required
def lease(request):
    if request.method == 'POST':
        car_id = request.POST.get('id')
        number_of_lease_str = request.POST.get('number_of_lease')

        # Check if number_of_lease_str is not empty and contains only digits
        if number_of_lease_str and number_of_lease_str.isdigit():
            number_of_lease = int(number_of_lease_str)     
        else:
            return JsonResponse({"error": "Invalid number_of_lease value. Must be a positive integer."}, safe=False, status=400) 

        try:
            car = Cars.objects.get(id=car_id)
            car.lease(number_of_lease)
            return JsonResponse({"message": "Car leased successfully."}, safe=False)
        except Cars.DoesNotExist:
            return JsonResponse({"JSON error": "Car not found."}, safe=False, status=404)
        except ValueError as ve:
            return JsonResponse({"value error": str(ve)}, safe=False, status=400)

    return JsonResponse({"request error": "Invalid request method."}, safe=False, status=400)


def update_lease(request,lease_id):
    leasing = get_object_or_404(Leasing, id=lease_id)

    if request.method == 'POST':
        form = UpdateLeasingForm(request.POST, instance=leasing)
        if form.is_valid():
            form.save()
            return redirect('crm:leasing_list')
    else:
        form = UpdateLeasingForm(instance=leasing)

    return render(request, 'crm/lease/lease_update_from.html', {'form': form, 'leasing': leasing})


@login_required
def delete_lease(request, lease_id):
    lease = get_object_or_404(Leasing, id=lease_id)
    if request.method == 'DELETE':
        lease.delete()
        return JsonResponse({'message': 'Lease deleted successfully'}, status=200)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)