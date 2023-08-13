vfrom django.conf.urls import url
from django.contrib import admin
from Remote_User import views as remoteuser
from amachine_learning_based_classification_ddosattacks import settings
from Service_Provider import views as serviceprovider
from django.conf.urls.static import static

urlpatterns = [
    url('admin/', admin.site.urls),
    # ... (Other URL patterns)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
