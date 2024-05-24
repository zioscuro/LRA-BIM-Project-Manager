from django.contrib.auth.mixins import UserPassesTestMixin

class StaffMixin(UserPassesTestMixin):
  """
  this mixin allow view access only to staff users
  """
  def test_func(self):
    return self.request.user.is_staff
