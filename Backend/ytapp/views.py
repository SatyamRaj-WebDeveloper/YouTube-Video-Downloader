from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from django.http import JsonResponse,FileResponse
import yt_dlp
import tempfile
import os

# Create your views here.
@api_view(['POST'])
def donloadVideo(request):
    url = request.data.get('url')
    if url :
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                ydl_opts = {
                'format': 'best',
                'outtmpl': os.path.join(temp_dir, '%(title)s.%(ext)s'),
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                file_path = ydl.prepare_filename(info)

            # Open the file after the temp_dir block to ensure it's accessible
            video_file = open(file_path, 'rb')
            response = FileResponse(
                video_file,
                as_attachment=True,
                filename=os.path.basename(file_path)
            )
            response['Content-Type'] = 'video/mp4'
            response['Access-Control-Allow-Origin'] = '*'  # CORS
            return response
        except Exception as e:
            print(f"Exception{str(e)}")
            return JsonResponse({'message':f"Exception!!!{str(e)}"})
    elif url is None:
        return JsonResponse({"Message":"Did not recieve url in Backend"})
    
