from django.shortcuts import render,redirect,get_object_or_404
from .forms import loginForm,contactForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.generic import DetailView,ListView
from .models import Products
# Create your views here.
from django.http import Http404
def contactView(request):
    form=contactForm()
    if request.method == "POST" :
        form=contactForm(request.POST,request.FILES)
        if form.is_valid():
            # print(form.cleaned_data["name"])
            # print(form.cleaned_data["email"])
            # print(form.cleaned_data["message"])
            return render(request,"contact.html",{"form":form,"text":"Succesfully submited"})
    return render(request,"contact.html",{"form":form})

def loginView(request):
    form_log=loginForm()
    if request.method == "POST" :
        form=loginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(username=username,password=password)
            if user is not None:
                print("loged in")
                return render(request,"login.html",{"form":form_log,"text":"Logged in Succesfully"})
            else :
                print("invalid credentials")


    return render(request,"login.html",{"form":form_log})

##############
class productFeaturedListView(ListView):
    model=Products
    template_name="product_list.html"
    #queryset=Products.objects.featured()
    queryset=Products.objects.all().featured()

class productFeaturedDetailView(DetailView):
    model=Products
    template_name="product_detail.html"
    queryset=Products.objects.all().featured()
class productDetailView(DetailView):
    model=Products
    template_name="product_details.html"
    # queryset=Products.objects.filter(title__icontains="mob")
    def get_object(self,*args,**kwargs):
        request=self.request
        pk =self.kwargs.get('pk')
        queryset=Products.objects.get_by_id(id=pk)
        if queryset is None:
            raise Http404("Product does not exist")
        return queryset

def product_detail_view(request,pk):
    # try:
    #     queryset=Products.objects.get(pk=pk)
    # except Products.DoesNotExist:
    #     raise Http404("Product does not exist")
    queryset=Products.objects.get_by_id(id=pk)
    if queryset is None:
        raise Http404("Product does not exist")

    # queryset=get_object_or_404(Products,pk=pk)
    context={
    "object":queryset
    }
    return render(request,"product_details.html",context)


class productListView(ListView):
    model=Products
    template_name="product_list.html"
    queryset=Products.objects.all()
    #
    # def get_context_data(self, **kwargs):
    #     context = super(productListView, self).get_context_data(**kwargs)
    #     #print(context)
    #     return context

def product_list_view(request):
    queryset=Products.objects.all()
    context={
    "object_list":queryset
    }
    return render(request,"product_list.html",context)
