from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import ContactForm
from .models import Profile, Work, Education, Experience, Software, Technical
from django.conf import settings
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse
import textwrap


class IndexView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by("-id")[0]
        work_data = Work.objects.order_by("-id")
        return render(request, 'app/index.html', {
            'profile_data': profile_data,
            'work_data': work_data
        })


class DetailView(View):
    def get(self, request, *args, **kwargs):
        work_data = Work.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/detail.html', {
            'work_data': work_data
        })
        
class AboutView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by('-id')[0]
        experience_data = Experience.objects.order_by('-id')
        education_data = Education.objects.order_by('-id')
        software_data = Software.objects.order_by('-id')
        technical_data = Technical.objects.order_by('-id')
        
        return render(request, 'app/about.html', {
            'profile_data': profile_data,
            'experience_data': experience_data,
            'education_data': education_data,
            'software_data': software_data,
            'technical_data': technical_data,
        })
                        
class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)
        return render(request, 'app/contact.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = 'otoiawase'
            contact = textwrap.dedent('''
                autoreply
                ---
                {name}
                {email}
                {message}
                ---
                ''').format(
                name=name,
                email=email,
                message=message
            )
        to_list = [email]
        bcc_list = [settings.EMAIL_HOST_USER]

        try:
            message = EmailMessage(subject=subject, body=contact, to=to_list, bcc=bcc_list)
            message.send()
        except BadHeaderError:
            return HttpResponse('mukouna header')

        return redirect('index')

        return render(request, 'app/contact.html', {
            'form': form
        })

class ThanksView(View):
    def post(self, request, *args, **kwargs):
        return render(request, 'app/thanks.html')


class ThanksView(View):
    def post(self, request, *args, **kwargs):
        return render(request, 'app/thanks.html')
        