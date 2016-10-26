from django import forms
from .models import Post, Comment, Stocks, Leaguetable

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

class StocksForm(forms.ModelForm):

    class Meta:
        model = Stocks
        fields = ('date', 'trans','symbol','qty','price')

class LeaguetableForm(forms.ModelForm):

    class Meta:
        model = Leaguetable
        fields = ('league','position','clubkor','played','win','draw','lose')

