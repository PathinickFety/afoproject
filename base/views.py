from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Participant, Team, Judge, Battle, JudgeScore
from .forms import (
    ParticipantForm, TeamForm, JudgeForm, BattleForm, JudgeScoreForm
)

def participant_list(request):
    participants = Participant.objects.all()
    return render(request, 'base/participant_list.html', {'participants': participants})

def participant_detail(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    return render(request, 'base/participant_detail.html', {'participant': participant})

def participant_create(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantForm()
    return render(request, 'base/participant_form.html', {'form': form})

def participant_update(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    if request.method == 'POST':
        form = ParticipantForm(request.POST, request.FILES, instance=participant)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantForm(instance=participant)
    return render(request, 'base/participant_form.html', {'form': form})

def participant_delete(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    if request.method == 'POST':
        participant.delete()
        return redirect('participant_list')
    return render(request, 'base/participant_confirm_delete.html', {'obj': participant})


# CRUD: Team Views
def team_list(request):
    teams = Team.objects.all()
    return render(request, 'base/team_list.html', {'teams': teams})

def team_create(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    else:
        form = TeamForm()
    return render(request, 'base/team_form.html', {'form': form})


# CRUD: Judge Views
def judge_list(request):
    judges = Judge.objects.all()
    return render(request, 'base/judge_list.html', {'judges': judges})


# CRUD: Battle Views
def battle_list(request):
    battles = Battle.objects.all()
    return render(request, 'base/battle_list.html', {'battles': battles})

def battle_create(request):
    if request.method == 'POST':
        form = BattleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('battle_list')
    else:
        form = BattleForm()
    return render(request, 'base/battle_form.html', {'form': form})

def battle_update(request, pk):
    battle = get_object_or_404(Battle, pk=pk)
    if request.method == 'POST':
        form = BattleForm(request.POST, request.FILES, instance=battle)
        if form.is_valid():
            form.save()
            return redirect('battle_list')
    else:
        form = BattleForm(instance=battle)
    return render(request, 'base/battle_form.html', {'form': form})

def battle_delete(request, pk):
    battle = get_object_or_404(Battle, pk=pk)
    if request.method == 'POST':
        battle.delete()
        return redirect('battle_list')
    return render(request, 'base/participant_confirm_delete.html', {'obj': battle})

def battle_detail(request, pk):
    battle = get_object_or_404(Battle, pk=pk)
    return render(request, 'base/battle_detail.html', {'battle': battle})


# Judges Voting and Battle Winner Calculation
def judge_vote(request, battle_id):
    battle = get_object_or_404(Battle, pk=battle_id)
    if request.method == 'POST':
        form = JudgeScoreForm(request.POST)
        if form.is_valid():
            form.save()
            # Check if all judges have voted
            total_scores = JudgeScore.objects.filter(battle=battle).count()
            if total_scores == 3 * 2:  # 3 judges, 2 teams
                battle.calculate_winner()
            return redirect('battle_list')
    else:
        form = JudgeScoreForm()
    return render(request, 'base/judge_vote_form.html', {'form': form, 'battle': battle})