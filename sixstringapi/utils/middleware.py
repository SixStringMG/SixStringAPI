from django.db import connection
from django.conf import settings

class DisableCSRF(object):
    def process_request(self, request):
        if request.path.startswith('/api/'):
            setattr(request, '_dont_enforce_csrf_checks', True)


class NoCacheAPI(object):
    def process_request(self, request):
        pass

    def process_response(self, request, response):
        if request.path.startswith('/api/'):
            response["Cache-Control"] = "no-cache, no-store, must-revalidate"
            response["Pragma"] = "no-cache"
            response["Expires"] = "0"

        return response
 
class QueryCountDebugMiddleware(object):
    """
    This middleware will log the number of queries run
    and the total time taken for each request (with a
    status code of 200). It does not currently support
    multi-db setups.
    """
    def process_request(self, request):
        pass

    def process_response(self, request, response):
        if getattr(settings, 'DEBUG', False):
            total_time = 0
 
            for query in connection.queries:
                query_time = query.get('time')
                if query_time is None:
                    # django-debug-toolbar monkeypatches the connection
                    # cursor wrapper and adds extra information in each
                    # item in connection.queries. The query time is stored
                    # under the key "duration" rather than "time" and is
                    # in milliseconds, not seconds.
                    query_time = query.get('duration', 0) / 1000
                total_time += float(query_time)
 
            print '{qtotal} queries run, total {time} seconds'.format(qtotal=len(connection.queries), time=total_time)
        return response