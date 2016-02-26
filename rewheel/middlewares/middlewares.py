import sys

from django.views.debug import technical_500_response


class SuperuserDebugMiddleware(object):
    def process_exception(self, request, exception):
        if request.user.is_superuser:
            return technical_500_response(request, *sys.exc_info())
