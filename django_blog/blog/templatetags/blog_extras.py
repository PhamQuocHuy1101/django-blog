from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe
from django.template import Library
from django.contrib.auth import get_user_model

from blog.models import Post

register = Library()
user_model = get_user_model()

@register.simple_tag(name='row')
def row(extends = ''):
    return format_html('<div class="row {}">', extends)

@register.simple_tag(name='endrow')
def endrow():
    return format_html('</div>')


@register.simple_tag(name='col')
def col(extends = ''):
    return format_html('<div class="col {}">', extends)

@register.simple_tag(name='endcol')
def endcol():
    return format_html('</div>')

@register.inclusion_tag('blog/post-list.html')
def recent_posts(post):
    posts = Post.objects.exclude(pk=post.pk)[:5]
    return {"title": "Recent Posts", "posts": posts}

@register.filter
def author_details(author, current_user=None):
    if not isinstance(author, user_model):
        return ""

    if author == current_user:
        return format_html("<strong>me</strong>")

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
       name = f"{author.username}"
    if author.email != None:
        email = author.email
        prefix = format_html('<a href="mailto:{}">', email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""
    return format_html("{}{}{}", prefix, name, suffix)


@register.filter
def todict(src, key):
    print(src)
    return src[key]