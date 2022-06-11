from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

from nkpro.registro.forms import Registro


class RegistroView(View):
    form_class = Registro
    initial = {'key': 'value'}
    template_name = 'registro/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='base:profile')

        return render(request, self.template_name, {'form': form})
