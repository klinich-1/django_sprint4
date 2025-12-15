from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import Page


# Templates for error pages referenced by tests
ERROR_403_TEMPLATE = '403csrf.html'
ERROR_404_TEMPLATE = '404.html'
ERROR_500_TEMPLATE = '500.html'


class AboutView(TemplateView):
    template_name = 'pages/about.html'


class RulesView(TemplateView):
    template_name = 'pages/rules.html'


class PageCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Page
    fields = ['title', 'slug', 'content']
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('pages:about')

    def test_func(self):
        return self.request.user.is_staff


class PageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Page
    fields = ['title', 'slug', 'content']
    template_name = 'pages/page_form.html'

    def test_func(self):
        return self.request.user.is_staff

    def get_success_url(self):
        # after editing redirect to the page URL if it exists, otherwise to about
        try:
            return reverse_lazy('pages:page_detail', kwargs={'slug': self.object.slug})
        except Exception:
            return reverse_lazy('pages:about')
