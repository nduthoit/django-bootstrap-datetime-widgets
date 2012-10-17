from bootstrap.forms import BootstrapMixin, Fieldset
from django import forms

from .widgets import BootstrapSplitDateTimeWidget, TimePickerWidget

from .models import YourModel

class YourForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = YourModel
#        layout = (
#            Fieldset("some_field", ),
#            Fieldset("some_other_field",),
#            )

    start_datetime = forms.DateTimeField(
        required=True,
        help_text="Start date and time.",
        widget=BootstrapSplitDateTimeWidget(
            attrs={
                'date_class':'datepicker-default',
                'time_class':'timepicker-default input-timepicker'
            }
        )
    )