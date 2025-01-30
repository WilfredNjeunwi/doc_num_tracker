from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Download
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def download_file(request):
    print(request.META.get('HTTP_X_CSRFTOKEN'))
    download, created = Download.objects.get_or_create(id=1)  # Singleton pattern
    download.count += 1
    download.save()

    # Replace with your document URL
    response = JsonResponse({"count": download.count})
    # response['Content-Disposition'] = 'attachment; filename="your_document.docx"'
    return response

def get_num_download(request):
    download = get_object_or_404(Download, id=1)
    response = JsonResponse({"count": download.count})
    return response

