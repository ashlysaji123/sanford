def superuser_only(function):
    def _inner(request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.is_superuser:
                return render(None, "403.html")
            return function(request, *args, **kwargs)

    return _inner
