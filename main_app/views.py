from django.shortcuts import render

finches = [
  {'name': 'Lolo', 'breed': 'house finch', 'description': 'red and brown', 'age': 3},
  {'name': 'Sachi', 'breed': 'american goldfinch', 'description': 'bright yellow with black wings', 'age': 2},
]
# Create your views here.

def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'finches/index.html', {
    'finches': finches
  })