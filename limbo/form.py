class SubscriptionCreate(TemplateResponseMixin, View):
    template_name = 'subscriptions/subscription_form.html'
    form_class = SubscriptionForm

    def get(self, *args, **kwargs):
        self.objects = None
        return self.render_to_response(self.get_context_data())

    def post(self, *args, **kwargs):
        self.objects = None
        form = self.get_form()

        if not form.is_valid():
            return self.form_invalid(form)
        return self.form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        self.object = form.save()

        # Send subscription email
        _send_mail('Confirmação de inscrição',
                   settings.DEFAULT_FROM_EMAIL,
                   self.object.email,
                   'subscriptions/subscription_email.txt',
                   {'subscription': self.object})

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return self.object.get_absolute_url()

    def get_form(self):
        if self.request.method == 'POST':
            return self.form_class(self.request.POST)
        return self.form_class()

    def get_context_data(self, **kwargs):
        context = dict(kwargs)
        context.setdefault('form', self.get_form())
        return context

new = SubscriptionCreate.as_view()
