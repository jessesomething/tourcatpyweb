from django import forms
from .models import Event
from .models import Merch

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('date','venue', 'city', 'state', 'price', 'text')
        # todo figure out easier date time fields
        # date = forms.DateTimeField(
        #     widget=SelectDateWidget(
        #         empty_label("Year","Month","Day"),),)

class MerchForm(forms.ModelForm):
    class Meta:
        model = Merch
        fields = ('name', 'merch_type', 'price', 'quantity')
