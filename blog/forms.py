from django import forms
from .models import Post, Comment, Leaguetable, Gamesetinfo, Gamesetproblem, Solvedproblem


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
        #fields = '__all__'
        #exclude = ()
class LeaguetableForm(forms.ModelForm):
	class Meta:
		model = Leaguetable
		fields = ('position','league','clubkor','played','win','draw','lose','gf','ga','gd','points',)

class GameForm(forms.ModelForm):
	class Meta:
		model = Gamesetinfo
		fields = ('gameset','game_type','rule_size','start_date','end_date')

class ProblemForm(forms.ModelForm):
	class Meta:
		model = Gamesetproblem
		fields = '__all__'

class HandleForm(forms.ModelForm):
	class Meta:
		model = Solvedproblem
		fields = ('handle',)
