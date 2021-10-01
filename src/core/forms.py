from django import forms

TYPE_CHOICES = (
    (1, "square"),
    (2, "round"),
)


class UploadFileForm(forms.Form):
    sphere_type = forms.ChoiceField(choices=TYPE_CHOICES)
    file = forms.FileField()
