from django.shortcuts import render
from .forms import SimpleForm
from django.contrib import messages
from .models import SimpleFormModel
from django.views.generic import CreateView, FormView


# Create your views here.

class SimpleFormView(CreateView):
    template_name = "simpleproject/index.html"
    form_class = SimpleForm
    success_url = '/'


    def form_valid(self, form):
        messages.success(self.request, "Uploaded Successfully")
        form.save()
        return super(SimpleFormView, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        objs = SimpleFormModel.objects.all().order_by('-id')
        objs_count = SimpleFormModel.objects.all().count()

        if objs_count == 0:
            context = {
                    "msg" : "No data uploaded yet",
                    "form": SimpleForm()
            }
        else:
            context = {
                "objs" : objs,
                "form" : SimpleForm()
            }
        return context







