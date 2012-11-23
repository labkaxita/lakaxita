from django.forms import ModelForm

from lakaxita.lost_found.models import Notification


class NotificationForm(ModelForm):
    class Meta:
        model = Notification
