from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    owned_projects = request.user.owned_projects.all()
    member = request.user.projects.all()
    return render(request, 'index.html', context={'owned_projects': owned_projects,
                                                  'member': member})
