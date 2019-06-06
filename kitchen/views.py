from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from flask import Flask, render_template, Response
from . import models
# Create your views here.
app = Flask(__name__)

def index(request):
    return render(request,"kitchen/templates/index.html",{})

def method(request):
    return render(request,"kitchen/templates/toprecipe/method.html",{})

def applegrumb(request):
    return render(request,"kitchen/templates/toprecipe/applegrumb.html",{})

def egg(request):
    return render(request,"kitchen/templates/toprecipe/egg.html",{})

def meatloaf(request):
    return render(request,"kitchen/templates/toprecipe/meatloaf.html",{})

def quinaoupma(request):
    return render(request,"kitchen/templates/toprecipe/quinaoupma.html",{})

def raw(request):
    return render(request,"kitchen/templates/toprecipe/raw.html",{})

def keema(request):
    return render(request,"kitchen/templates/toprecipe/keema.html",{})

def baigan(request):
    return render(request,"kitchen/templates/toprecipe/baigan.html",{})

def fish(request):
    return render(request,"kitchen/templates/toprecipe/fish.html",{})

def aloo(request):
    return render(request,"kitchen/templates/toprecipe/aloo.html",{})

def Apolo(request):
    return render(request,"kitchen/templates/Indian/Apolo.html",{})

def cchiken(request):
    return render(request,"kitchen/templates/Indian/cchiken.html",{})

def dal(request):
    return render(request,"kitchen/templates/Indian/dal.html",{})

def noodle(request):
    return render(request,"kitchen/templates/Indian/noodle.html",{})

def pork(request):
    return render(request,"kitchen/templates/Indian/pork.html",{})

def sahi(request):
    return render(request,"kitchen/templates/Indian/sahi.html",{})

def saunpa(request):
    return render(request,"kitchen/templates/Indian/saunpa.html",{})

def sejwan(request):
    return render(request,"kitchen/templates/Indian/sejwan.html",{})

def idiya(request):
    return render(request,"kitchen/templates/Indian/idiya.html",{})


def nan(request):
    return render(request,"kitchen/templates/Indian/nan.html",{})
