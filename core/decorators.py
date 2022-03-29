from django.shortcuts import render


def superuser_only(function):
    def _inner(request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.is_superuser:
                return render(None, "403.html")
            return function(request, *args, **kwargs)

    return _inner


def checking_dashboard_access(function):
    def _inner(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if (user.is_sales_executive or user.is_merchandiser):
                return render(None, "403.html")
            return function(request, *args, **kwargs)

    return _inner
