from django.contrib.admin.sites import AdminSite

class TestPostAdmin:
 def test_excerpt(self):
    site = AdminSite()
    post_admin = admin.PostAdmin(models.Post,site)
    obj = mixer.blend('MainApp.Post',body="Hello World")
    result = post_admin.excerpt(obj)
    assert result == 'Hello', 'Should return first few characters'
