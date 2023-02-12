import django
from django import forms


def hidden_field(required=True):
    return forms.CharField(widget=forms.HiddenInput(), required=required)


def boolean_field(label, required=True, initial=False):
    return forms.BooleanField(label=label, required=required, initial=initial)


def char_field(label, max_length, required=True):
    return forms.CharField(label=label, max_length=max_length, widget=forms.TextInput(
        attrs={'class': 'form-control btn-square'}), required=required)


def int_field(label, required=True, max_value=None, min_value=None):
    return forms.IntegerField(label=label, max_value=max_value, min_value=min_value,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control btn-square'}),
                              required=required,
                              )


def text_area(label, max_length, required=True):
    return forms.CharField(label=label, max_length=max_length,
                           widget=forms.Textarea(attrs={'class': 'form-control btn-square'}),
                           required=required
                           )


def date_field(label, default_date=django.utils.timezone.now, required=True):
    return forms.DateField(label=label, widget=forms.DateInput(
        attrs={'class': 'form-control btn-square', 'type': 'date'}),
                           initial=default_date,
                           required=required
                           )


def date_time_field(label, default_time=django.utils.timezone.now, required=True, field_name=''):
    return forms.DateTimeField(label=label, widget=forms.DateTimeInput(
        attrs={'class': 'form-control digits', 'type': 'datetime-local'}),
                           initial=default_time,
                           required=required
                           )


def model_choice_field_single(label, queryset, initial=0, required=True):
    return forms.ModelChoiceField(label=label,
                                  widget=forms.Select(
                                      attrs={
                                          'class': 'form-control btn-square js-example-basic-single'
                                      }),
                                  queryset=queryset,
                                  initial=0,
                                  required=required
                                  )


def model_choice_field_multiple(label, queryset, initial=0, required=True):
    return forms.ModelMultipleChoiceField(label=label,
                                          widget=forms.SelectMultiple(
                                              attrs={
                                                  'class': 'form-control btn-square js-example-basic-multiple'
                                              }),
                                          queryset=queryset,
                                          required=required
                                          )


def model_choice_field_multiple_checkbox(label, queryset, initial=0, required=True):
    return forms.ModelMultipleChoiceField(label=label,
                                          widget=forms.CheckboxSelectMultiple,
                                          queryset=queryset,
                                          required=required
                                          )


def radio_field(label, initial, required=True, choices=[], onchange=''):
    return forms.ChoiceField(
        label=label,
        widget=forms.RadioSelect(
            attrs={'onchange': onchange + ";"}),
        choices=choices,
        initial=initial)


def file_field(label, multiple=True, required=False):
    return forms.FileField(
        label=label,
        widget=forms.ClearableFileInput(
            attrs={
                'multiple': multiple,
                'class': 'form-control btn-square mb-2'
            }
        ),
        required=required
    )


def ip_address_field(label, required=False):
    return forms.GenericIPAddressField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control btn-square mb-2'
            }
        ),
        required=required
    )


