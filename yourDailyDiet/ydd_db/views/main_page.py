from django.shortcuts import render
def main_page(request):
    return render(
        request=request,
        template_name='main_page.html',
        context={'name': request.user.username}
    )

