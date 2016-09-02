from django.test import TestCase
from models import Bookmark, Tag
from forms import BookmarkForm

class TagTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(name="tagtestowy")

    def test_tag(self):
        testowy = Tag.objects.get(name="tagtestowy")
        self.assertEqual(testowy.name, "tagtestowy")

class BookmarkTestCase(TestCase):
    def setUp(self):
        sample_user = User.objects.create()
        sample_tag = Tag.objects.create(name="shit")
        Bookmark.save(
            url="http://www.rdc.pl",
            title="Radio RDC",
            description="Mazowiecka stacja radiowa",
            is_public=True,
            date_created="2016-09-01",
            date_updated="2016-09-01",
            owner=sample_user
            tags=sample_tag,
        )

    def test_bookmarks(self):
        test_bookmark = Bookmark.objects.get(url="http://www.rdc.pl")
        self.assertEqual(test_bookmark.title, "Radio RDC")
