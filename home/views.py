from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def finder(request):
    if request.method == "GET":
        searchQuery = request.GET.get("search")
        
        data = {
            "search": searchQuery
        }
        print(request.GET)
        return render(request, 'finder.html', data)