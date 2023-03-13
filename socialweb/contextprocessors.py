from socialweb.models import Posts,Comments
def activities(request):
    if request.user.is_authenticated:
        cnt=Posts.objects.filter(user=request.user).count()
        ant=Comments.objects.filter(user=request.user).count()
        return {"qcnt":cnt,"acnt":ant}
    else:
        return {"qcount":0}