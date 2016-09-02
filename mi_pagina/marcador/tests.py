from django.test import TestCase
from models import Bookmark, Tag
from forms import BookmarkForm
from django.contrib.auth.models import User

class TagTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(name="tagtestowy")

    def test_tag(self):
        testowy = Tag.objects.get(name="tagtestowy")
        self.assertEqual(testowy.name, "tagtestowy")


class BookmarkTestCase(TestCase):
    def setUp(self):
        first_user = User.objects.create()
        print(first_user, User.objects.count())
        Bookmark.objects.create(
            url="http://www.rdc.pl",
            title="Radio RDC",
            description="Mazowiecka stacja radiowa",
            is_public=True,
            date_created="2016-09-01",
            date_updated="2016-09-01",
            owner=first_user
            # tags="shit"
        )

    def test_bookmarks(self):
        rdc = Bookmark.objects.get(url="http://www.rdc.pl")
        self.assertEqual(rdc.title, "Radio RDC")
