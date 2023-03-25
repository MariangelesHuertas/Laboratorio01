from django.shortcuts import render

def suma(request):
    if request.method == 'POST':
        num1 = int(request.POST['num1'])
        num2 = int(request.POST['num2'])
        resultado = num1 + num2
        return render(request, 'suma.html', {'resultado': resultado})
    else:
        return render(request, 'suma.html')

