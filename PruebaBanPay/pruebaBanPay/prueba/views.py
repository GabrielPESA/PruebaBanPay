from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd

# Create your views here.
def Tabla1(request):
    tablaOriginal = pd.read_csv("./templates/archivo_original.csv")
    my_dict = {
        "df": tablaOriginal.to_html()
    }
    return render(request, 'Tabla1.html', context=my_dict)

def Tabla2(request):
    tablaNativos = pd.read_excel("./templates/Nombres_Nativos_Asia.xlsx")
    my_dict = {
        "df": tablaNativos.to_html()
    }
    return render(request, 'Tabla2.html', context=my_dict)

def Inicio(request):
    return render(request, 'index.html')