from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse
from django.views import generic
from django_tables2 import SingleTableView

from .models import Location, Owner, SparePart
from .tables import PartsTable
from .forms import SparePartForm

class PartsView(SingleTableView):
    model = SparePart
    table_class = PartsTable
    paginate_by = 15
    template_name = 'rd/index.html'

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class DetailView(generic.DetailView):
    model = SparePart
    template_name = 'rd/part_detail.html'

# update
class PartUpdateView(generic.UpdateView):
    model = SparePart
    fields = ['name', 'type', 'dop', 'owner', 'location']
    template_name = 'rd/part_form.html'

# add
def create_view(request):
    form = SparePartForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('rd:index')
    context = {
        'form': form,
    }
    return render(request, "rd/part_create.html", context)

# delete
class PartDeleteView(generic.DeleteView):
    model = SparePart
    template_name = 'rd/part_confirm_delete.html'
    success_url = '/rd/'

# API Views
from rest_framework import viewsets
from .serializers import SparePartSerializer

class SparePartViewSet(viewsets.ModelViewSet):
    queryset = SparePart.objects.all()
    serializer_class = SparePartSerializer
