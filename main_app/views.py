from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Decoration
from .forms import FeedingForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def finches_index(request):
    finches = Finch.objects.all()  # Retrieve all finches
    return render(request, 'finches/index.html', {
        'finches': finches
    })


def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    id_list = finch.decorations.all().values_list('id')
  # Now we can query for toys whose ids are not in the list using exclude
    decorations_finch_doesnt_have = Decoration.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
    # include the cat and feeding_form in the context
    'finch': finch, 'feeding_form': feeding_form,
    'decorations': decorations_finch_doesnt_have
  })

def add_feeding(request, finch_id):
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the finch_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)


class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'breed', 'habitat']

class FinchUpdate(UpdateView):
    model = Finch
    # Let's disallow the renaming of a finch by excluding the name field!
    fields = ['breed', 'description', 'habitat']


class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'

class DecorationList(ListView):
  model = Decoration

class DecorationDetail(DetailView):
  model = Decoration

class DecorationCreate(CreateView):
  model = Decoration
  fields = '__all__'

class DecorationUpdate(UpdateView):
  model = Decoration
  fields = ['name', 'color']

class DecorationDelete(DeleteView):
  model = Decoration
  success_url = '/decorations'

def assoc_decoration(request, finch_id, decoration_id):
  pass
  print('apple')
  Finch.objects.get(id=finch_id).decorations.add(decoration_id)
  return redirect('detail', finch_id=finch_id)

def unassoc_decoration(request, finch_id, decoration_id):
  print('banana')
  Finch.objects.get(id=finch_id).decorations.remove(decoration_id)
  return redirect('detail', finch_id=finch_id)
