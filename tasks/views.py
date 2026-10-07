from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Task, Category, Note, Priority, SubTask

from .forms import (
    TaskForm,
    CategoryForm,
    PriorityForm,
    SubTaskForm,
    NoteForm,
)


class HomePageView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["total_tasks"] = Task.objects.count()

        context["pending_tasks"] = Task.objects.filter(
            status="Pending"
        ).count()

        context["in_progress_tasks"] = Task.objects.filter(
            status="In Progress"
        ).count()

        context["completed_tasks"] = Task.objects.filter(
            status="Completed"
        ).count()

        return context





class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = "tasks"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.GET.get("q")

        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )

        sort_by = self.request.GET.get("sort_by")

        allowed = [
            "title",
            "deadline",
            "status",
        ]

        if sort_by in allowed:
            qs = qs.order_by(sort_by)
        else:
            qs = qs.order_by("deadline")

        return qs


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("task-list")


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("task-list")


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy("task-list")




class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "category_list.html"
    context_object_name = "categories"


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "management_form.html"
    success_url = reverse_lazy("category-list")


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "management_form.html"
    success_url = reverse_lazy("category-list")


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = "management_confirm_delete.html"
    success_url = reverse_lazy("category-list")




class PriorityListView(LoginRequiredMixin, ListView):
    model = Priority
    template_name = "priority_list.html"
    context_object_name = "priorities"


class PriorityCreateView(LoginRequiredMixin, CreateView):
    model = Priority
    form_class = PriorityForm
    template_name = "management_form.html"
    success_url = reverse_lazy("priority-list")


class PriorityUpdateView(LoginRequiredMixin, UpdateView):
    model = Priority
    form_class = PriorityForm
    template_name = "management_form.html"
    success_url = reverse_lazy("priority-list")


class PriorityDeleteView(LoginRequiredMixin, DeleteView):
    model = Priority
    template_name = "management_confirm_delete.html"
    success_url = reverse_lazy("priority-list")



# NOTE CRUD


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = "note_list.html"
    context_object_name = "notes"


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = "management_form.html"
    success_url = reverse_lazy("note-list")


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "management_form.html"
    success_url = reverse_lazy("note-list")


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = "management_confirm_delete.html"
    success_url = reverse_lazy("note-list")



class SubTaskListView(LoginRequiredMixin, ListView):
    model = SubTask
    template_name = "subtask_list.html"
    context_object_name = "subtasks"


class SubTaskCreateView(LoginRequiredMixin, CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = "management_form.html"
    success_url = reverse_lazy("subtask-list")


class SubTaskUpdateView(LoginRequiredMixin, UpdateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = "management_form.html"
    success_url = reverse_lazy("subtask-list")


class SubTaskDeleteView(LoginRequiredMixin, DeleteView):
    model = SubTask
    template_name = "management_confirm_delete.html"
    success_url = reverse_lazy("subtask-list")



@login_required
def dashboard_view(request):

    total_tasks = Task.objects.count()

    pending_tasks = Task.objects.filter(
        status="Pending"
    ).count()

    in_progress_tasks = Task.objects.filter(
        status="In Progress"
    ).count()

    all_categories = Category.objects.all()

    recent_notes = Note.objects.order_by("-id")[:5]

    context = {
        "total_tasks": total_tasks,
        "pending_tasks": pending_tasks,
        "in_progress_tasks": in_progress_tasks,
        "categories": all_categories,
        "notes": recent_notes,
    }

    return render(request, "dashboard.html", context)