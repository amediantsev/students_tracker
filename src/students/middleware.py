import time

from students.models import Logger


class AdminLoggingMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, callback, callback_args, callback_kwargs):
        start = time.time()
        if request.path.startswith('/admin/'):
            Logger.objects.create(path=request.path,
                                  method=request.method,    # mch.METHOD_CHOICE_REVERSED[request.method]
                                  user_id=request.user.id,
                                  time_delta=time.time() - start,
                                  )
