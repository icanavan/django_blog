from django.shortcuts import render
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import Http404, HttpResponse, HttpResponseRedirect
from blogging.models import Post


class BloggingListView(ListView):
    #model = Post # according to HW should be queryset. must include filter or exclude and order_by
    # model = Post is equivalent to queryset = Post.objects.all()
    queryset = Post.objects.exclude(published_date__exact=None).order_by('-published_date')
    template_name = 'blogging/list.html'


class BloggingDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'

# def list_view(request):
#     published = Post.objects.exclude(published_date__exact=None) this one is done
#     posts = published.order_by('-published_date') this one is done
#     template = loader.get_template('blogging/list.html') this one is done
#     context = {'posts': posts}
#     body = template.render(context)
#     return HttpResponse(body, content_type="text/html")

# def detail_view(request, post_id):
#     published = Post.objects.exclude(published_date__exact=None)
#     try:
#         post = published.get(pk=post_id)
#     except Post.DoesNotExist:
#         raise Http404
#     context = {'post': post}
#     return render(request, 'blogging/detail.html', context)

# def stub_view(request, *args, **kwargs):
#     body = "Stub View\n\n"
#     if args:
#         body += "Args:\n"
#         body += "\n".join(["\t%s" % a for a in args])
#     if kwargs:
#         body += "Kwargs:\n"
#         body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
#     return HttpResponse(body, content_type="text/plain")