from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from polls.models import Vote, VoteOption


def index(request):
    vote_list = Vote.objects.all()
    context = {
        'vote_list': vote_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, vote_id):
    try:
        vote = Vote.objects.get(id=vote_id)
        vote_options = VoteOption.objects.filter(vote_id=vote_id)
    except Vote.DoesNotExist:
        raise Http404("Vote does not exist")
    return render(request, 'polls/detail.html', {'vote': vote, 'vote_options': vote_options})


def results(request, vote_id):
    vote = get_object_or_404(Vote, pk=vote_id)
    vote_options = VoteOption.objects.filter(vote_id=vote_id)
    return render(request, 'polls/results.html', {'vote': vote, 'vote_options': vote_options})


def vote(request, vote_id):
    vote = get_object_or_404(Vote, pk=vote_id)
    try:
        selected_choice = VoteOption.objects.get(id=request.POST['choice'])
    except (KeyError, Vote.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'vote': vote,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.count += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(vote.id, )))

