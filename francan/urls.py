from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views
from home import views as custom_views

urlpatterns = [
    path('django-admin/', admin.site.urls),

    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),

    path('search/', search_views.search, name='search'),
    path('shelf/<int:id>/', custom_views.shelf, name="shelf"),
    path('<int:id>/add_product/', custom_views.addproduct,
         name="add Shelf Product"),
    path('add_product/', custom_views.newproduct),
    path('sell_product/<int:id>', custom_views.sellitem),
    path('handle_product_sale/', custom_views.handle_product_sale),
    path('add_new_client/', custom_views.add_client),
    path('add_shelf/', custom_views.add_shelf),
    path('add_rent/', custom_views.add_rent),
    path('rent_payments/', custom_views.rent_payments),
    path('addClient/', custom_views.handle_add_client),
    path('addShelf/', custom_views.handle_add_shelf),
    path('addRent/', custom_views.handle_add_rent),

]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
