from django.http import HttpResponse
from django.shortcuts import render_to_response
from ApoBlogDjango.models import Content, Comments

__author__ = 'abdullah'


def index(request):
    c = Content.objects.all()
    return render_to_response('Index/index.html', {'result': c})


def detailView(request):
    subject_id = int(request.GET.get('id'))
    subjectContent = Content.objects.get(id=subject_id)
    c = Comments.objects.filter(SID=subject_id).order_by('id')
    return render_to_response('Index/DetailView.html', {'result': subjectContent, 'comments': c})



def comments(request):
    if request.is_ajax():
        subject_id = request.POST['sid']
        c = Comments.objects.filter(SID=subject_id).order_by('id')
        return render_to_response('Comments/PartialComments.html', {'comments': c})
    else:
        c = Comments.objects.all().order_by('id').reverse()
        return render_to_response('Comments/Comments.html', {'comments': c})


def leaveComment(request):
     if request.method == 'POST':
        subject_id = request.POST['sid']
        comment = request.POST['comment']
        s = Comments(SID=subject_id, Message=comment)
        s.save()
        return HttpResponse("true")