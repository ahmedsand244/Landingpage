import urllib.parse
from django import template

register = template.Library()

@register.filter
def whatsapp_link(project_title, number="201099632832"):
    message = f"Hello, I want to inquire about the project: {project_title}. Please provide more details about pricing and deliverables."
    encoded_message = urllib.parse.quote(message)
    return f"https://wa.me/{number}?text={encoded_message}"


@register.filter
def youtube_embed(url):
    if not url:
        return ""
    if "watch?v=" in url:
        return url.replace("watch?v=", "embed/")
    elif "youtu.be/" in url:
        # e.g., https://youtu.be/abc -> https://www.youtube.com/embed/abc
        video_id = url.split("youtu.be/")[-1].split("?")[0]
        return f"https://www.youtube.com/embed/{video_id}"
    return url
