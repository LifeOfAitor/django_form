from django.dispatch import receiver
from django.shortcuts import render
from .forms import ContactForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


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

            # store data on the database
            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)

            # send email with confirmation
            send_mail(first_name, email)

            # show message on index when form sent correctly
            messages.success(request, "form submitted successfully")
        else:
            # This will print any form validation errors
            print(form.errors)
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")


def send_mail(name, user_email):
    message_body = f"""
        A new job application was submitted. Thank you {name}.
    """
    email_message = EmailMessage("Form submission confirmation",
                                 message_body, to=[user_email])
    email_message.send()