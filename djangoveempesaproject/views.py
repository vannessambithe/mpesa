from django.shortcuts import render


def payuser(request):
    return render(request, 'payment.html')