from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/assoc_decoration/<int:decoration_id>/', views.assoc_decoration, name='assoc_decoration'),
    path('finches/<int:finch_id>/unassoc_decoration/<int:decoration_id>/', views.unassoc_decoration, name='unassoc_decoration'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('decorations/', views.DecorationList.as_view(), name='decorations_index'),
    path('decorations/<int:pk>/', views.DecorationDetail.as_view(), name='decorations_detail'),
    path('decorations/create/', views.DecorationCreate.as_view(), name='decorations_create'),
    path('decorations/<int:pk>/update/', views.DecorationUpdate.as_view(), name='decorations_update'),
    path('decorations/<int:pk>/delete/', views.DecorationDelete.as_view(), name='decorations_delete'),
    path('finches/<int:finch>/add_feeding/', views.add_feeding, name='add_feeding')
    
]
    
