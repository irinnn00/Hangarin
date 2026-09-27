from django import forms

from .models import (
    Task,
    SubTask,
    Note,
)


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task

        fields = [
            "title",
            "description",
            "status",
            "deadline",
            "priority",
            "category",
        ]


class SubTaskForm(forms.ModelForm):

    class Meta:
        model = SubTask

        fields = [
            "title",
            "status",
            "task",
        ]


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note

        fields = [
            "task",
            "content",
        ]