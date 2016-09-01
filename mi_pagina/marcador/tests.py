from django.test import TestCase
from models import Bookmark, Tag
from forms import BookmarkForm

class TagTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(name="tagtestowy")

    def test_tag(self):
        testowy = Tag.objects.get(name="tagtestowy")
        self.assertEqual(testowy.name, "tagtestowy")
# class BookmarkTestCase(TestCase):
#     def setUp(self):
        # form = BookmarkForm(data={
        #     'url': "http://www.rdc.pl",
        #     'title': "Radio RDC",
        #     'description': "Mazowiecka stacja radiowa",
        #     'is_public': True,
        #     'date_created': "2016-09-01",
        #     'date_updated': "2016-09-01",
        #     'owner_id': 1
        # })
        # form.save()

        # Bookmark.objects.create(
        # Bookmark.save(
        #     url="http://www.rdc.pl",
        #     title="Radio RDC",
        #     description="Mazowiecka stacja radiowa",
        #     is_public=True,
        #     date_created="2016-09-01",
        #     date_updated="2016-09-01",
        #     owner="rosz"
        # tags=["shit"],
        # )
        # Bookmark.object.create(
        #     url=
        #     title=
        #     description=
        #     is_public=
        #     date_created=
        #     date_updated=
        #     owner=
        #     tags=
        # )
        # Bookmark.object.create(
        #     url=
        #     title=
        #     description=
        #     is_public=
        #     date_created=
        #     date_updated=
        #     owner=
        #     tags=
        # )

    # def test_bookmarks(self):
    #     rdc = Bookmark.objects.get(url="http://www.rdc.pl")
    #     self.assertEqual(rdc.title(), "Radio RDC")
