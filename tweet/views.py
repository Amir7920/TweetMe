from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello world</h1>")
    template_name = "pages/home.html"
    return render(request, template_name, context={}, status=200)


def tweet_list_view(request, *args, **kwargs):
    """
    REST API VIEW 
    Consume by JavaScript or Swift or Java or IOS/Android
    return json data
    """
    qs = Tweet.objects.all()
    data = {
        'response': [
            {'id': x.id, 'content': x.content} for x in qs
        ]
    }
    return JsonResponse(data)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW 
    Consume by JavaScript or Swift or Java or IOS/Android
    return json data
    """
    data = {
        "id": tweet_id,
    }
    status = 200

    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
        # data['image_path'] = obj.image.url
    except:
        # raise Http404(f"Tweet with id = '{tweet_id}' is not found")
        data['message'] = "Not found"
        status = 404

    # return HttpResponse(f"<h1># {tweet_id} - {obj.content}")
    return JsonResponse(data, status=status)  # json.dumps content_type='application/json'
