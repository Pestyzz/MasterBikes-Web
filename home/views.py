from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def finder(request):
    if request.method == "GET":
        return render(request, 'finder.html')
    else:
        searchQuery = request.POST.get("search")
        
        data = {
            "search": searchQuery
        }
        print(request.POST)
        return render(request, 'finder.html', data)