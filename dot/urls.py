"""dot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from drivers import views as driver_views
from examiner import views as examiner_views
from examiner.views import DriverDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^driver_registration/$', driver_views.driver_registration),
    url(r'^driver_health_history/$', driver_views.driver_health_history),
    # url(r'^examiner/[0-9]+/$', examiner_views.examiner),
    url(r'^examiner/[0-9]+/drivers/$', examiner_views.examiner_drivers),
    url(r'^examiner_login/$', examiner_views.examiner_login),
    # url(r'^examiner/[0-9]+/details/$', examiner_views.examiner_details),
    url(r'^examiner_logout/$', examiner_views.examiner_logout),
    url(r'^examiner_register/$', examiner_views.register),
    url(r'^examiner/[0-9]+/exam/driver/[0-9]+/$', examiner_views.exam_questions),
    url(r'^examiner/[0-9]+/exam/$', examiner_views.exam_questions),
    url(r'^examiner/[0-9]+/calendar/$', examiner_views.exam_calendar),
    url(r'^examiner/[0-9]/driver/[0-9]+/$', examiner_views.driver_history),
    url(r'^examiner/[0-9]/driver/[0-9]+/$', examiner_views.driver_history),
    url(r'^examiner/[0-9]/details/$', examiner_views.examiner_information),
    url(r'^examiner/[0-9]/update_details/$', examiner_views.examiner_information_update),
    url(r'^examiner/driver_search/$', examiner_views.driver_search),
    url(r'^examiner/driver_search/clear/$', examiner_views.driver_clear_search),
    url(r'^examiner/[0-9]+/new_exam_from_calendar/$', examiner_views.new_exam_from_calendar),
    url(r'^examiner/update_exam/$', examiner_views.update_exam),
    url(r'^examiner/delete_exam/$', examiner_views.delete_exam),
    url(r'^examiner/submit_exam/$', examiner_views.submit_exam_questions),
    url(r'^examiner/driver_detail/(?P<pk>[0-9]+)/$', DriverDetailView.as_view(template_name="driver_detail.html")),
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
