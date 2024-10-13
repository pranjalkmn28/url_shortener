from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.utils import timezone
from .models import URL
from .forms import URLForm

class URLCreateView(View):
    template_name = 'create_url.html'

    def get(self, request):
        form = URLForm()
        print(form)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            url.save()
            return render(request, 'url_detail.html', {'url': url})
        return render(request, self.template_name, {'form': form})


class URLRedirectView(View):
    def get(self, request, short_url):
        url = URL.objects.filter(short_url=short_url).order_by('-created_at').first()
        # url = get_object_or_404(URL, short_url=short_url)
        if url.is_expired:
            return render(request, 'expired.html')
        return redirect(url.original_url)


class URLDetailView(View):
    template_name = 'url_detail.html'

    def get(self, request, short_url):
        # url = get_object_or_404(URL, short_url=short_url)
        url = URL.objects.filter(short_url=short_url).order_by('-created_at').first()
        return render(request, self.template_name, {'url': url})
