from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .forms import SalaryForm

from  . modules.salary import check_salary
from . modules.graph import Graph

def index(request):
    return render(request, 'salary_calc/index.html')

def results(request):
    return render(request, 'salary_calc/results.html')

def get_salary(request):
    if request.method == 'POST':
        form = SalaryForm(request.POST or None)
        if form.is_valid():
            print(request.POST)

            param1_brutto = request.POST.get('param1')
            param2_brutto = request.POST.get('param2')
            param3_brutto = request.POST.get('param3')
            param4_brutto = request.POST.get('param4')
            param5_brutto = request.POST.get('param5')
            param6_brutto = request.POST.get('param6')
            par1 = check_salary(request.POST.get('param1'))
            par2 = check_salary(request.POST.get('param2'))
            par3 = check_salary(request.POST.get('param3'))
            par4 = check_salary(request.POST.get('param4'))
            par5 = check_salary(request.POST.get('param5'))
            par6 = check_salary(request.POST.get('param6'))
            graph = Graph(par1, par2, par3, par4, par5, par6, param1_brutto, param2_brutto, param3_brutto, param4_brutto, param5_brutto, param6_brutto)


            graph.draw_graph('wykres.png')

            context = {
                "par1": par1,
                "par2": par2,
                "par3": par3,
                "par4": par4,
                "par5": par5,
                "par6": par6,
                "param1_brutto": param1_brutto,
                "param2_brutto": param2_brutto,
                "param3_brutto": param3_brutto,
                "param4_brutto": param4_brutto,
                "param5_brutto": param5_brutto,
                "param6_brutto": param6_brutto,
            }
            return render(request, 'salary_calc/results.html', context)

    else:
        form = SalaryForm()

    return render(request, 'salary_calc/get_salary.html', { 'form': form})
