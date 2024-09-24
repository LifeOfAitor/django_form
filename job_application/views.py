from django.shortcuts import render

# redirects to index.html when the server launches
def index(request):
    return render(request, "index.html")
