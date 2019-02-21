from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect
from django.contrib import messages
from django.http import HttpResponseBadRequest, HttpResponseForbidden
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import OmeFile
from .forms import OmeForm

import markdown2


def markdown_create(request):
    data = {'markdown_text': ''}
    if request.is_ajax():
        if request.method == 'POST':
            gelen = request.POST.get('markdown_text')
            html_text = markdown2.markdown(gelen)
            data.update({'markdown_text': html_text})
            return JsonResponse(data=data, safe=False)

    form = OmeForm(data=request.POST or None)
    mdfile = OmeFile.objects.all()
    if form.is_valid():
        if 'save' in request.POST:
            gelen = request.POST.get('markdown_text')
            html_text = markdown2.markdown(gelen)
            new_ome = form.save(commit=True)
            new_ome.html_text = html_text
            new_ome.user = request.user
            new_ome.save()

    return render(request, 'markdown_convert.html', context={'form': form, 'mdfile': mdfile})

"""
def markdown_view(request, slug):
    omefile = get_object_or_404(OmeFile, slug=slug)
    form = OmeForm(instance=omefile, data=request.POST or None)
    if form.is_valid():
        if 'view' in request.POST:
            new_ome = form.save(commit=False)
            markdown_text = form.cleaned_data.get('markdown_text')
            new_ome.html_text = markdown2.markdown(markdown_text)
            return render(request, 'markdown_view.html', context={'form': form, 'new_ome': new_ome, 'slug': slug})
        else:
            new_ome = form.save(commit=False)
            markdown_text = form.cleaned_data.get('markdown_text')
            new_ome.html_text = markdown2.markdown(markdown_text)
            form.save()
            msg = 'Tebrikler %s isimli gönderiniz başarı ile güncellendi.' % (omefile.title)
            messages.success(request, msg, extra_tags='info')
            return render(request, 'markdown_view.html', context={'slug': slug, 'form': form, 'omefile': omefile})
    return render(request, 'markdown_view.html', context={'slug': slug, 'form': form, 'omefile': omefile})
"""

def markdown_delete(request, slug):
    omefile = get_object_or_404(OmeFile, slug=slug)
    omefile.delete()
    return HttpResponseRedirect(reverse('markdown-create'))
