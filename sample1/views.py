from django.shortcuts import render
from django.core.urlresolvers import reverse
# Create your views here.
from sample1.models import Information


def add_new_information(request):
    if request.method == "POST":
        if 'full_name' in request.POST:
            information = Information.objects.create(full_name='pouria eini')
            return render(request, 'information/index.html', {'full_name': information.full_name})
        else:
            return reverse('sample1:add-new-information')
    else:
        return render(request, 'information/add_new_information.html', {})
