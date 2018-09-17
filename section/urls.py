from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
url(r"^contact/$",views.contactView,name="contact"),
url(r"^login/$",views.loginView,name="login"),
url(r"^product/$",views.productListView.as_view(),name="product_list"),
url(r"^product_featured/$",views.productFeaturedListView.as_view(),name="product_list"),
url(r"^product_featured/(?P<pk>\d+)$",views.productFeaturedDetailView.as_view(),name="product_featured_detail"),
url(r"^product_f/$",views.product_list_view,name="product_list"),
url(r"^product/(?P<pk>\d+)$",views.productDetailView.as_view(),name="product_detail"),
url(r"^product_f/(?P<pk>\d+)$",views.product_detail_view,name="product_detail"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
