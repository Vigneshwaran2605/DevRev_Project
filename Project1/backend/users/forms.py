import datetime
import dateutil
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Flight

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class TimeInput(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = [
            forms.Select(choices=[(str(i).zfill(2), str(i).zfill(2)) for i in range(1, 13)]),
            forms.Select(choices=[(str(i).zfill(2), str(i).zfill(2)) for i in range(0, 60, 15)]),
            forms.Select(choices=[('AM', 'AM'), ('PM', 'PM')]),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            hour, minute = value.split(':')
            if int(hour) > 12:
                am_pm = 'PM'
                hour = str(int(hour) - 12).zfill(2)
            elif int(hour) == 12:
                am_pm = 'PM'
            else:
                am_pm = 'AM'
            return [hour, minute, am_pm]
        return [None, None, None]

    def value_from_datadict(self, data, files, name):
        hour, minute, am_pm = self.widgets[0].value_from_datadict(data, files, f'{name}_0'), self.widgets[1].value_from_datadict(data, files, f'{name}_1'), self.widgets[2].value_from_datadict(data, files, f'{name}_2')
        if hour and minute and am_pm:
            if am_pm == 'PM' and hour != '12':
                hour = str(int(hour) + 12).zfill(2)
            elif am_pm == 'AM' and hour == '12':
                hour = '00'
            return f'{hour}:{minute}'
        return None



class FlightForm(forms.ModelForm):
        date = forms.DateField(widget=forms.SelectDateWidget, initial=datetime.date.today())    
        time = forms.CharField(widget=TimeInput(), required=True)
        available_seats = forms.IntegerField(initial=60)
  
        class Meta:
            model = Flight
            fields = ['date', 'time', 'available_seats']




