from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'home/home.html')

def vps(request):
    return render(request, 'home/vps.html')

def site(request):
    return render(request, 'home/site.html')

def contact(request):
    return render(request, 'home/contact.html')

# note: normalment on a pas besoin de ces methode
# todo: faire en sorte d'afficher la page selon la requete url
def lireArticle(request):
    return render(request, 'home/home.html')

def lirePage(request):
    return render(request, 'home/home.html')


# on recupere la liste des offres vps et la page vps et on envoie le tout
# c'est le template (la page vps) qui affiche les offres
#def pageVps(request):
#    return render(request, "home/vps.html")
#
def pageWeb(request):
    return render(request, "home/home.html")
