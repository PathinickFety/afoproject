from django import forms
from .models import Participant, Team, Judge, Battle, JudgeScore

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'age', 'dance_style', 'picture']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['participant_one', 'participant_two']

class JudgeForm(forms.ModelForm):
    class Meta:
        model = Judge
        fields = ['name']

class BattleForm(forms.ModelForm):
    class Meta:
        model = Battle
        fields = ['title', 'team_one', 'team_two', 'judges']

class JudgeScoreForm(forms.ModelForm):
    class Meta:
        model = JudgeScore
        fields = [
            'battle', 'judge', 'team',
            'musicality', 'originality', 'creativity', 'energy', 'collision',
            'battle_spirit', 'move', 'technique', 'timing', 'combo'
        ]
