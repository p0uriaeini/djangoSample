from django.conf.urls import url, include
from . import views

urlpatterns = [
    # url(r'^$', admin.site.urls),
    url(r'^add/', views.add_new_information, name='add-new-information'),
    url(r'^list/', views.get_list_of_informaion, name='get-information-list'),
]
