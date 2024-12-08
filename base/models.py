from django.db import models


class Participant(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    dance_style = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='participants/', blank=True, null=True, default='jocker face.jpg')

    def __str__(self):
        return self.name


class Team(models.Model):
    participant_one = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='team_one')
    participant_two = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='team_two')

    def __str__(self):
        return f"{self.participant_one.name} & {self.participant_two.name}"
    

class Judge(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Battle(models.Model):
    title = models.CharField(max_length=200)
    team_one = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='battles_as_team_one')
    team_two = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='battles_as_team_two')
    judges = models.ManyToManyField(Judge, related_name='battles')
    winner = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='won_battles')

    def __str__(self):
        return f"{self.title}: {self.team_one} vs {self.team_two}"

    def calculate_winner(self):
        team_one_score = sum(
            score.total_score for score in self.scores.filter(team=self.team_one)
        )
        team_two_score = sum(
            score.total_score for score in self.scores.filter(team=self.team_two)
        )

        if team_one_score > team_two_score:
            self.winner = self.team_one
        elif team_two_score > team_one_score:
            self.winner = self.team_two
        else:
            self.winner = None  # In case of a tie
        self.save()


class JudgeScore(models.Model):
    battle = models.ForeignKey(Battle, on_delete=models.CASCADE, related_name='scores')
    judge = models.ForeignKey(Judge, on_delete=models.CASCADE, related_name='scores')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='scores')
    musicality = models.PositiveIntegerField(default=0)
    originality = models.PositiveIntegerField(default=0)
    creativity = models.PositiveIntegerField(default=0)
    energy = models.PositiveIntegerField(default=0)
    collision = models.PositiveIntegerField(default=0)
    battle_spirit = models.PositiveIntegerField(default=0)
    move = models.PositiveIntegerField(default=0)
    technique = models.PositiveIntegerField(default=0)
    timing = models.PositiveIntegerField(default=0)
    combo = models.PositiveIntegerField(default=0)

    @property
    def total_score(self):
        return sum([
            self.musicality,
            self.originality,
            self.creativity,
            self.energy,
            self.collision,
            self.battle_spirit,
            self.move,
            self.technique,
            self.timing,
            self.combo
        ])

    def __str__(self):
        return f"Judge {self.judge.name} - {self.team.participant_one} & {self.team.participant_two} - Total: {self.total_score}"
