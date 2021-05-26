import hello.views
from django.urls import path, include
from django.contrib import admin
import classifier.views
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()


# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("dashboard/", hello.views.db, name="dashboard"),
    path("about/", hello.views.about, name="about"),
    path("classifier/", classifier.views.index, name="classifier"),
    path("classifier/results/", classifier.views.results,
         name="classifier-results"),
    path("techniques/", classifier.views.techniques,
         name="classifier-techniques"),
    path('techniques/<int:technique_id>',
         classifier.views.techniquesDetails, name='techniqueDetails'),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
