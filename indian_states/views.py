from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from indian_states.models import State
from indian_states.forms import StateForm
# Create your views here.

class StateListView(ListView):
    model = State
    template_name = 'state_list.html'

class StateDetailView(DetailView):
    model = State
    template_name = 'state_detail.html'

class StateCreateView(CreateView):
    model = State
    form_class = StateForm
    template_name = 'state_form.html'
    success_url = reverse_lazy('state_list')

class StateUpdateView(UpdateView):
    model = State
    form_class = StateForm
    template_name = 'state_form.html'
    success_url = reverse_lazy('state_list')

class StateDeleteView(DeleteView):
    model = State
    success_url = reverse_lazy('state_list')
