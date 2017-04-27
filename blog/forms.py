from django import forms
from .models import Post, Comment, Leaguetable, Gamesetinfo, Gamesetproblem, Solvedproblem


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)
		# fields = '__all__'
		# exclude = ()


class LeaguetableForm(forms.ModelForm):
    class Meta:
        model = Leaguetable
        fields = ('position', 'league', 'clubkor', 'played', 'win', 'draw', 'lose', 'gf', 'ga', 'gd', 'points',)


class GameForm(forms.ModelForm):
    class Meta:
        model = Gamesetinfo
        fields = ('gameset', 'game_type', 'rule_size', 'start_date', 'end_date')


class ProblemForm(forms.ModelForm):
    #gameset = forms.ModelChoiceField(queryset=Gamesetinfo.objects.all())
    rule_num = forms.IntegerField()
    problem = forms.IntegerField()
    language = forms.CharField()

    class Meta:
    	model = Gamesetproblem
    	fields = ('rule_num','problem','language',)
    # def __init__(self, *args, **kwargs):
    # accountid = kwargs.pop('accountid', None)
    # super(AccountDetailsForm, self).__init__(*args, **kwargs)

    #def save(self, request, gamesetproblem):
    #    gamesetproblem.gameset = self.cleaned_data['gameset']
	#	gamesetproblem.rule_num = self.cleaned_data['rule_num']
	#	gamesetproblem.problem = self.cleaned_data['problem']
	#	gamesetproblem.language = self.cleaned_data['language']
	#	gamesetproblem.save()
	#	return gamesetproblem


class HandleForm(forms.ModelForm):
    class Meta:
        model = Solvedproblem
        fields = ('handle',)
