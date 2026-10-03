from django.shortcuts import render, get_object_or_404
from .models import MainPage, Department, Program, ExchangeProgram


def home(request):
    page_data = MainPage.objects.first()
    return render(request, 'core/home.html', {'page_data': page_data})


def program_list(request):
    programs = Program.objects.all()
    return render(request, 'core/program_list.html', {'programs': programs})


def program_detail(request, pk):
    program = get_object_or_404(Program, pk=pk)
    return render(request, 'core/program_detail.html', {'program': program})


def department_list(request):
    departments = Department.objects.all()
    return render(request, 'core/department_list.html', {'departments': departments})


def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'core/department_detail.html', {'department': department})


def exchange_list(request):
    programs = ExchangeProgram.objects.all().order_by('deadline')
    return render(request, 'core/exchange_list.html', {'programs': programs})
