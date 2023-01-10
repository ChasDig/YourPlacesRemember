from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, FormView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import MemoryPlacesModel
from .forms import MemoryCreateForm


# ----- Places memories views ----- #


class MemoriesListView(ListView):
    """ View: Display all users memories """

    model = MemoryPlacesModel
    template_name = "places_memory/memory_list.html"
    context_object_name = "memory_list"

    success_url = reverse_lazy("memory_list")
    login_url = 'memory_list'

    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Get contex_data for users memories:
        :param object_list: -
        :param kwargs: -
        :return: if user is authenticated - return user memories, else - Nothing([])
        """

        context = super().get_context_data(**kwargs)

        # Get all users memories from QuerySet:
        if self.request.user.is_authenticated:

            context["memory_list"] = self.get_queryset()
            context["memory_list_carousel"] = self.get_queryset()

        return context

    def get_queryset(self):
        """
        If user authenticated - return his memories:
        :return: user memories or []
        """
        if self.request.user.is_authenticated:

            return self.request.user.memory_list.all()
        else:
            return []


class MemoryDetailView(LoginRequiredMixin, DetailView):
    """ View: Display detail users memories """

    model = MemoryPlacesModel
    template_name = "places_memory/memory_detail.html"
    queryset = MemoryPlacesModel.objects.all()
    context_object_name = "memory_detail"

    slug_field = 'slug'

    def get_context_data(self, **kwargs):

        if self.object.user_id == self.request.user.id:
            context = super().get_context_data(**kwargs)

            return context
        else:
            return self.handle_no_permission()


class MemorySearchList(LoginRequiredMixin, ListView):
    """ View: Search memory """

    template_name = "places_memory/memory_list.html"
    context_object_name = "memory_list"

    paginate_by = 2

    def get_queryset(self):

        if self.request.user.is_authenticated:

            return MemoryPlacesModel.objects.filter(
                    title__icontains=self.request.GET.get('q')
                ).filter(
                user=self.request.user
            )

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:

            context["memory_list_carousel"] = MemoryPlacesModel.objects.filter(
                user=self.request.user
            ).order_by(
                'data_published_memory'
            )

        context['q'] = f"q={self.request.GET.get('q')}&"

        return context


class MemoryCreateView(LoginRequiredMixin, CreateView, FormView):
    """ View: Create memory """

    template_name = "places_memory/memory_create.html"
    form_class = MemoryCreateForm

    success_url = reverse_lazy("memory_list")

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        return context

    def post(self, request, *args, **kwargs):

        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):

        user_memory = form.save(commit=False)

        user_memory.user = self.request.user

        return super().form_valid(form=form)


class MemoryDeleteView(LoginRequiredMixin, DeleteView):
    """ View: Delete memory """

    model = MemoryPlacesModel
    template_name = "places_memory/memory_list.html"

    success_url = reverse_lazy("memory_list")

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """

        self.object = self.get_object()

        if self.request.user.id != self.object.user_id:
            return self.handle_no_permission()

        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
