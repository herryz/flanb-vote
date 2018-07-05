from django.shortcuts import render

from vote.models import Vote, VoteOption


def vote(request):
    objs = Vote.objects.all()
    context = {'vote_list': objs}
    return render(request, 'vote/vote.html', context)


