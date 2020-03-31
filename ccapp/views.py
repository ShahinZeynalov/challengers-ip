from django.shortcuts import render
from .models import Question, Applicant, Message
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import FormMixin
from .forms import ContactForm
from django.urls import reverse_lazy
from .emails import send_feedback_email

class HomePageView(FormMixin, TemplateView):
    template_name = 'index.html'
    model = Message
    form_class = ContactForm
    success_url = reverse_lazy('challengers:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = Question.objects.all()
        context['applicants'] = Applicant.objects.filter(status=1)
        context['empty_cards'] = range(4 - Applicant.objects.filter(status=1).count())
        return context

    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            form.save()
            sender_email = request.POST.get('sender_email')
            sender_name = request.POST.get('sender_name')
            send_feedback_email(sender_email, sender_name)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self,form):
        context = super().form_invalid(form)
        return context
