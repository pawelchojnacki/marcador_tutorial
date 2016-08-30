from django.forms import ModelForm

from .models import bookmark_user


class BookmarkForm(ModelForm):
    class Meta:
        model = Bookmark
        exlude = ("date_created", "date_updated", "owner")
