from django import forms
from django.contrib.auth import get_user_model
from .models import Post, Comment, Category, Location


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'pub_date', 'category', 'location', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only allow selecting published categories and published locations
        try:
            self.fields['category'].queryset = Category.objects.filter(is_published=True)
        except Exception:
            pass
        try:
            self.fields['location'].queryset = Location.objects.filter(is_published=True)
        except Exception:
            pass


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class EditUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email']
