from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from django.http import JsonResponse,FileResponse
from pytube import YouTube
import os

# Create your views here.
@api_view(['POST'])
def donloadVideo(request):
    url = request.data.get('url')
    if url :
        try:
            yt = YouTube(url)
            print('Yt',yt)
            stream = yt.streams.all()
            if not stream:
                print("No streams Available")
            else:
                print("Stream",stream)
            file_path = stream.download()
            print('file_path:',file_path)
            return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=stream.default_filename)
        except Exception as e:
            return JsonResponse({'message':f"Exception!!!{str(e)}"})
    elif url is None:
        return JsonResponse({"Message":"Did not recieve url in Backend"})
    
