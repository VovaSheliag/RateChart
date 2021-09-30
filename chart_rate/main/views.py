from django.shortcuts import render, redirect
from django.views import View
from .forms import RateSavingForm
from .models import RateHistory


class MainView(View):
    """
    View class to visualize html template, validate form and get data from DB
    Also to process errors in post request
    """
    def get(self, request):
        form = RateSavingForm()
        date = RateHistory.objects.order_by('date')  # Ordered rate history by data
        return render(request, 'main/rate_template.html', context={'form': form, 'date': date})

    def post(self, request):
        form = RateSavingForm(request.POST)
        date = RateHistory.objects.all()
        if form.is_valid():
            form.save()
            return redirect('/')
        context = {
            'errors': form.errors,
            'form': form,
            'date': date
        }
        return render(request, 'main/rate_template.html', context=context)  # Render errors on the main page
