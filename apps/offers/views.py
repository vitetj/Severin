from django.shortcuts import render
from django.template import Template
from offers.models import *


# Create your views here.
# on recupere la liste des offres vps et la page vps et on envoie le tout
# c'est le template (la page vps) qui affiche les offres
def pageVps(request):
    res = Vps.objects.all()
    data = {}
    data['listeVps'] = res
    return render(request, "offers/vps.html", data)

def pageWeb(request):
    return render(request, "offers/web.html")
