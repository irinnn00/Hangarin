from django import forms

from .models import (
    Task,
    Category,
    Priority,
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


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category

        fields = [
            "name",
        ]


class PriorityForm(forms.ModelForm):

    class Meta:
        model = Priority

        fields = [
            "name",
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