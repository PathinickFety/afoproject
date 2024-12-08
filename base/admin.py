from django.contrib import admin
from .models import Participant, Team, Judge, Battle, JudgeScore

admin.site.register(Participant)
admin.site.register(Team)
admin.site.register(Judge)
admin.site.register(Battle)
admin.site.register(JudgeScore)