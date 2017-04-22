from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Stocks(models.Model):
    date = models.TextField(blank=True, null=True)
    trans = models.TextField(blank=True, null=True)
    symbol = models.TextField(blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stocks'

class Leaguetable(models.Model):
    position = models.IntegerField(primary_key=True)
    league = models.TextField()
    clubkor = models.TextField(db_column='clubKor')  # Field name made lowercase.
    clubeng = models.TextField(db_column='clubEng')  # Field name made lowercase.
    played = models.IntegerField()
    win = models.IntegerField()
    draw = models.IntegerField()
    lose = models.IntegerField()
    gf = models.IntegerField()
    ga = models.IntegerField()
    gd = models.IntegerField()
    points = models.IntegerField()

    class Meta:
        #managed = False
        db_table = 'leagueTable'
        unique_together = (('position', 'league'),)

class Solvedproblem(models.Model):
    handle = models.TextField(primary_key=True)
    problem = models.TextField()
    last_date = models.DateTimeField(default=timezone.now)
    language = models.TextField()

    class Meta:
        #managed = False
        db_table = 'solvedProblem'
        unique_together = (('handle', 'problem'),)

class Gamesetinfo(models.Model):
    gameset = models.IntegerField(primary_key=True)
    game_type = models.IntegerField(null=False)
    rule_size = models.IntegerField(null=False)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return u'{0}'.format(self.gameset)
    class Meta:
        #managed = False
        db_table = 'gamesetInfo'


class Gamesetproblem(models.Model):
    gameset = models.ForeignKey('Gamesetinfo')
    #gameset = models.IntegerField(primary_key=True)
    rule_num = models.IntegerField()
    problem = models.IntegerField()
    language = models.TextField()

    def save():
        a=a

    class Meta:
        #managed = False
        db_table = 'gamesetProblem'
        unique_together = (('gameset', 'rule_num'),)
