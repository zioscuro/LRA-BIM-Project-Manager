from django.contrib.auth.mixins import UserPassesTestMixin

class StaffMixin(UserPassesTestMixin):
  """
  this mixin allow projects and BIM models creation only to staff users
  """

  def test_func(self):
    return self.request.user.is_staff
