from django import forms
from .models import HealthPost,WelcomeMsgRecipients

DISTRICTS= [
    ('', 'Please Choose District'),
    ('', 'Bugesera'),
    ('', 'Burera'),
    ('', 'Gakenke'),
    ('', 'Gasabo'),
    ('', 'Gatsibo'),
    ('', 'Gicumbi'),
    ('', 'Gisagara'),
    ('', 'Huye'),
    ('', 'Kamonyi'),
    ('', 'Karongi'),
    ('', 'Kayonza'),
    ('', 'Kicukiro'),
    ('', 'Kirehe'),
    ('', 'Muhanga'),
    ('', 'Musanze'),
    ('', 'Ngoma'),
    ('', 'Ngororero'),
    ('', 'Nyabihu'),
    ('', 'Nyagatare'),
    ('', 'Nyamagabe'),
    ('', 'Nyamasheke'),
    ('', 'Nyanza'),
    ('', 'Nyarugenge'),
    ('', 'Nyaruguru'),
    ('', 'Rubavu'),
    ('', 'Ruhango'),
    ('', 'Rulindo'),
    ('', 'Rusizi'),
    ('', 'Rutsiro'),
    ('', 'Rwamagana'),
    ]

class HealthPostForm(forms.ModelForm):
    class Meta:
        model = HealthPost
        exclude = ["user"]
        widgets = {
            'district_name': forms.Select(choices=DISTRICTS)
        }
       
# class ProfileForm(forms.ModelForm):
    # class Meta:
    #     model = Profile
    #     exclude = ['user']
        
# class ProjectsForm(forms.ModelForm):
#     class Meta:
#         model = Projects
#         exclude = []

# class RatingForm(forms.ModelForm):
#     class Meta:
#         model = Rating2
#         exclude = []
#         # widgets = {
#         #     'content': forms.CheckboxSelectMultiple(),
#         # }
#         # content=forms.CharField(widget=forms.Textarea)
class HealthPostForm2(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')