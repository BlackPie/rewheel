class UserReceivingFormMixin(object):
    """
    Mixin for user receiving in forms.
    It should be used with UserPassingViewMixin
    """
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(UserReceivingFormMixin, self).__init__(*args, **kwargs)


class EqualFieldsFormMixin(object):
    """
    This mixin gets all fields names mentioned in self.equal_fields
    and check these fields data equality.
    """
    equal_fields = []

    def clean(self):
        cleaned_data = super(EqualFieldsFormMixin, self).clean()
        fields_data = [cleaned_data[x] for x in self.equal_fields]
        return len(set(fields_data)) <= 1
