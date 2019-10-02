from django.shortcuts import render

# Create your views here.
from .forms import Registration_form
def registration_view(request):
    # import form object
    registration_form = Registration_form()
    # check if it's a POST request i.e. form submission
    if request.method == 'POST':
        # Check the form is valid
        if registration_form.is_valid():
            # register user!
            return render(request, 'coreapp/success.html')
        else:
            message = {'message': 'Error!'}
            return render(request, 'coreapp/registration.html',{'registration_form': registration_form,
                                                                'message': message})
    else:
        return render(request, 'coreapp/registration.html',{'registration_form': registration_form})
