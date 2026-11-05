from blog.models import Comment, Post
from blog.moderation import is_toxic
from django import forms
from django.core.exceptions import ValidationError

MODERATION_ERROR = (
    'Комментарий не проходит модерацию. '
    'Пожалуйста, сформулируйте мысль корректнее.'
)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'category', 'pub_date', 'location', 'image')
        widgets = {
            'pub_date': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={'type': 'datetime-local'}),
        }


class CommentForm(forms.ModelForm):

    def clean_text(self):
        text = self.cleaned_data['text']
        if is_toxic(text):
            raise ValidationError(MODERATION_ERROR)
        return text

    class Meta:
        model = Comment
        fields = ('text',)
