class UserPassingViewMixin(object):
    """
    Mixin for user passing in views.
    It should be used with UserPassingFormMixin
    """
    def get_form_kwargs(self):
        kwargs = super(UserPassingViewMixin, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs