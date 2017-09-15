from django import forms



class CommentForm(forms.ModelForm):
    class Meta:
        fields = [
            'name',
            'email',
            'url',
            'text',
        ]