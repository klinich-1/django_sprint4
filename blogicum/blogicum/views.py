from django.shortcuts import render


def custom_404(request, exception=None):
    return render(request, 'pages/404.html', status=404)


def custom_500(request):
    return render(request, 'pages/500.html', status=500)


def custom_403(request, exception=None):
    return render(request, 'pages/403csrf.html', status=403)


def csrf_failure(request, reason=""):
    # Django's CsrfViewMiddleware can be configured to use this view via
    # the CSRF_FAILURE_VIEW setting. Use the CSRF-specific template.
    return render(request, 'pages/403csrf.html', status=403)
