# Create your views here.
from django.http import HttpResponse
from .tasks import async_time_consuming_task

def index(request):

    # Do a time consuming task
    async_time_consuming_task.delay(5)

    html_content = """
    <h1 style="text-align: center;">This is your site's index. It now runs immediately and our time consuming task is taken care of in the background!</h1>
    """
    return HttpResponse(html_content)
