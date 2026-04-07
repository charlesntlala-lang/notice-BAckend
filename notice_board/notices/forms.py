from django import forms
from .models import Notice

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'content', 'category', 'priority', 'publish_date', 'expiry_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'publish_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'expiry_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
        labels = {
            'title': 'Notice Title',
            'content': 'Content',
            'category': 'Category',
            'priority': 'Priority',
            'publish_date': 'Publish Date (optional)',
            'expiry_date': 'Expiry Date (optional)',
        }
        help_texts = {
            'title': 'Keep it short and clear',
            'content': 'Full announcement details',
            'publish_date': 'Leave blank for immediate publish',
            'expiry_date': 'Leave blank for no expiry',
        }
