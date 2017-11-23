from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView

from .models import Project


class ProjectDetail(DetailView):
    model = Project
    template_name = 'project.html'


class ProjectCreate(CreateView):
    model = Project
    fields = ('name',)
    template_name = 'project_form.html'
    success_url = reverse_lazy('portal:index')

    def form_valid(self, form):
        self.object = Project.create_project(self.request, form)
        return HttpResponseRedirect(self.get_success_url())


class ProjectUpdate(UpdateView):
    model = Project


class ProjectDelete(DeleteView):
    model = Project
