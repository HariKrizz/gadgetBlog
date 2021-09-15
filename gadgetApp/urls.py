from django.urls import path
from gadgetApp import views

urlpatterns = [

    path('',views.gadgetHome,name='home'),
    path('gadget/<int:g_id>',views.gadgetDetails,name='gadgsdetails'),
    path('addGadget/',views.addGadget,name='add'),
    path('update/<int:g_id>',views.updateGadget,name='update'),
    path('delete/<int:g_id>',views.deleteGadget,name='delete')
]