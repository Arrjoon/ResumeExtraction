
from django.urls import path
from . import views 


urlpatterns = [
    
    # path('',views.,name="ranking_resume"),
     path('',views.ranking_resume,name="job_description"),
    path('export_jobs_to_csv/', views.export_resumes_to_csv, name='export_jobs_to_csv'),
]
