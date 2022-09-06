from django.db import models
from django.db.models import BooleanField, CharField, DateField, IntegerField
from django.urls import reverse


class Trade(models.Model):
    """
    Default custom user model for inv_dashboard.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    date = DateField(auto_now_add=True)
    start_network = CharField(max_length=15)
    start_ticker = CharField(max_length=10)
    start_amount = IntegerField()
    start_usd_amt = IntegerField()
    post_platform = CharField(max_length=30)
    post_amount = CharField(max_length=10)
    post_tickers = CharField(max_length=30)
    post_usd_amt = IntegerField()
    end_usd_amt = IntegerField()
    end_date = DateField()
    profit_loss_percent = IntegerField()
    profit_loss_usd_amt = IntegerField()
    is_active = BooleanField(default=True)
    deadline = DateField()

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
