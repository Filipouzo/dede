from .models import BlogPost
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404


# Create your views here.

def email_check(user):
    return user.email.endswith("@gmail.com")


def index(request):
    return render(request, "blog/base.html")


# @login_required
@user_passes_test(email_check)
def article(request, numero_article):
    if numero_article in ["01", "02", "03"]:
        return render(request, f"blog/article_{numero_article}.html")
    return render(request, "blog/article_not_found.html")


def blog_post(request, numero_post):
    blog_post_by_id = get_object_or_404(BlogPost, pk=numero_post)

    return render(request, "blog/post.html", context={"blog_post": blog_post_by_id})


def blog_list(request):
    all_blog_posts = BlogPost.objects.all()
    return render(request, "blog/post_list.html", context={"all_blog_posts": all_blog_posts})
