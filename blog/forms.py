from django import forms
from .models import Post, Comment, Leaguetable


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
