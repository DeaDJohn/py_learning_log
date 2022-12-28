from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields =['text']
        labels = {'text': 'Texto'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80, 'class': 'form-input appearance-none block w-full bg-lime-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white'}),
        'title': forms.Textarea(attrs={'rows': 2, 'class': 'form-input appearance-none block w-full bg-lime-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white'}),
        }


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'text', 'imagen']
        labels = {'title': 'Título','text': 'Texto', 'imagen': 'Imagen destacada'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80, 'class': 'form-input appearance-none block w-full bg-lime-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white'}),
        'title': forms.Textarea(attrs={'rows': 2, 'class': 'form-input appearance-none block w-full bg-lime-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white'}),
        }