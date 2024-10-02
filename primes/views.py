from django.shortcuts import render

# Create your views here.

def input_page(request):
    return render(request, 'primes/input.html')



def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def output_page(request):
    if request.method == 'POST':
        input_number = int(request.POST.get('number'))
        primes = [i for i in range(2, input_number + 1) if is_prime(i)]
        return render(request, 'primes/output.html', {'primes': primes, 'input_number': input_number})
    return render(request, 'primes/output.html', {'primes': []})
