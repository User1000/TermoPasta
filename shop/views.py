from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import *
# Create your views here.

class ItemListView(ListView):
    model = Item
    template_name = "shop/list.html"

    def get_queryset(self):
        qs = super(ItemListView, self).get_queryset()
        try:
            return qs.filter(category=Category.objects.filter(slug=self.kwargs['slug']))
        except:
            return qs.filter(category=Category.objects.filter(slug='termopasta'))

class ItemDetailView(DetailView):
    model = Item
    template_name = "shop/item.html"
    # assert False
    # def get_queryset(self):
    #     qs = super(ItemDetailView, self).get_queryset()
    #     # assert False, self.kwargs['slug']
    #     return qs.filter(category=self.kwargs['slug'])


@csrf_exempt
def add_order(request, item_id):
    if (request.method == 'POST'):
        # id = request['id']
        # tel = request['usrtel']
        quan = request.POST.get('quantity')
        cl_tel = request.POST.get('usrtel')
        cl_name = request.POST.get('name')
        cl_email = request.POST.get('email')
# id:
# quantity:1
# name:rtytr
# usrtel:656575
# email:
        cl, created = Client.objects.get_or_create(phone=cl_tel)
        if created:
            cl.name = cl_name
            cl.email = cl_email

        o = Order(client=cl)
        o.save()

        item = Item.objects.get(pk=item_id)
        oi = OrderItem(item=item, order=o, quantity=quan)
        oi.save()


        # request[]

        return HttpResponse(cl_tel)
    return HttpResponse('ok')