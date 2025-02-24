from django import forms
from blog.models import Post

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category','title','description', 'content', 'art_image')