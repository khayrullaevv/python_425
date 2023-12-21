from django.urls import include, path

from pages.views import blog_page_view, contact_page_view, about_page_view, home_page_view

app_name = "pages"

urlpatterns = [
    path("blogs/", blog_page_view, name="blogs"),
    path("contact/", contact_page_view, name="contact"),
    path("about/", about_page_view, name="about"),
    path('products/', include("products.urls", namespace="products")),
    path("", home_page_view, name="home"),
]