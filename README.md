###Summary

Django widgets and field for getting bootstrap-timepicker and bootstrap-datepicker working with a split datetime field. This allows you to render a form with a Bootstrap style datepicker for the date portion of the field and a Bootstap style timepicker for the time portion of the field.

### Usage

1. Include the JS and CSS from bootstrap-timepicker and bootstrap-datepicker (see below)
2. install via pip using `pip install -e git://github.com/stholmes/django-bootstrap-datetime-widgets.git#egg=bootstrap-datetime-widgets`
3. See static/example.js for example jQuery implementation.
4. See forms.py for example usage, e.g.

	widget=BootstrapSplitDateTimeWidget(
			attrs={
				'date_class':'datepicker-default',
				'time_class':'timepicker-default input-timepicker'
			}
	)


To just use only the timepicker, pass `widget=TimePickerWidget` into your field.

Make sure your datepicker JS object is setup correctly to work with the accepted date formats on your field, e.g.:

	$('.datepicker-default').datepicker({
    	format:'yyyy-mm-dd'
    });

###Dependencies:

* [bootstrap-timepicker](http://www.github.com/jdewit/bootstrap-timepicker)
* [bootstrap-datepicker](http://www.eyecon.ro/bootstrap-datepicker)
* [django-bootstrap](https://github.com/earle/django-bootstrap) - *optional*

###TODO

* Make this more modular and easier to configure
* Version of widget / field without timepicker for use with DateField
* Demo page
