from django.views import View
from django.shortcuts import render


class HomePageView(View):
    def get(self, request):
        # Retrieve data from models or perform custom queries
        # data1 = Model1.objects.all()
        # data2 = Model2.objects.filter(some_field="value")

        context = {
            # "data1": data1,
            # "data2": data2,
        }

        return render(request, "home.html", context)
