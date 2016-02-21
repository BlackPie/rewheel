class UserReceivingFormMixin(object):
    """
    Mixin for user receiving in forms.
    It should be used with UserPassingViewMixin
    """
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(UserReceivingFormMixin, self).__init__(*args, **kwargs)
