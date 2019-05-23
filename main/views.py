from django.shortcuts import render, redirect
import youtube_dl
# from django.urls import reverse_lazy
# from django.views.generic import FormView
# from .models import Song
from .forms import DownloadForm

# class DownloadView(FormView):
#     form_class = DownloadForm
#     model = Song
#     template_name = 'index.html'
#     success_url = reverse_lazy('index')
#
#     def form_valid(self, form):
#         link = form.cleaned_data.get('url')
#         ydl_opts = {
#             'format': 'bestaudio/best',
#             'postprocessors': [{
#                 'key': 'FFmpegExtractAudio',
#                 'preferredcodec': 'mp3',
#                 'preferredquality': '192',
#             }]}
#         with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([link])
#         return super(DownloadView, self).form_valid(form)
#
#     def post(self, request, *args, **kwargs):
#         """
#         Handle POST requests: instantiate a form instance with the passed
#         POST variables and then check if it's valid.
#         """
#         form = self.get_form()
#         link = form.get('url')
#         ydl_opts = {
#             'format': 'bestaudio/best',
#             'postprocessors': [{
#                 'key': 'FFmpegExtractAudio',
#                 'preferredcodec': 'mp3',
#                 'preferredquality': '192',
#             }]}
#         if form.is_valid():
#             with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#                 ydl.download([link])
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

def download(request):
    form = DownloadForm()
    if request.method == "POST":
        form = DownloadForm(request.POST) #if no files
        if form.is_valid():
            form.save()
            video_url = form.cleaned_data.get('url')
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                # ydl.download([video_url])
                info = ydl.extract_info(video_url, download=False)

                return redirect(info['formats'][0]['url'])
    context = {
        'form': form,
    }
    return render(request, "index.html", context)