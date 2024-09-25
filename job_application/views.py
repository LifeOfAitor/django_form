from django.shortcuts import render
from .forms import ContactForm


# redirects to index.html when the server launches
# django implements "request" by default, no need to import
def index(request):
    # get the values of the form when submit is clicked (GET -> POST)
    if request.method == "POST":
        form = ContactForm(request.POST)
        # validate the form
        if form.is_valid():
            # the names have to correspond with the names in index.html
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]
        else:
            # This will print any form validation errors
            print(form.errors)
    return render(request, "index.html")
