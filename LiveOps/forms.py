from django import forms

class ReportForm(forms.Form):
    event = forms.CharField(max_length=100)
    author = forms.CharField(max_length=40)
    datetime = forms.DateTimeField()
    diagnosis = forms.CharField(widget=forms.Textarea(attrs={'rows':'4', 'cols': '100'}))
    impact = forms.CharField(widget=forms.Textarea(attrs={'rows':'4', 'cols': '100'}))
    resolution  = forms.CharField(widget=forms.Textarea(attrs={'rows':'4', 'cols': '100'}))
    responsibility = forms.CharField(widget=forms.Textarea(attrs={'rows':'4', 'cols': '100'}))
    actionable = forms.BooleanField(required=False)
    action = forms.CharField(widget=forms.Textarea(attrs={'rows':'4', 'cols': '100'}))
