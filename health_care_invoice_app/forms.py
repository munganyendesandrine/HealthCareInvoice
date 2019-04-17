from django import forms
from .models import HealthPost,Patient,WelcomeMsgRecipients

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

types_hc=[
    ('', 'HC/CS'),
    ('', 'HP/PS'),
    ]

class HealthPostForm(forms.ModelForm):
    class Meta:
        model = HealthPost
        exclude = ["user"]
        widgets = {
            'district_Name': forms.Select(choices=DISTRICTS),
            'health_Facility_Type': forms.RadioSelect(choices=types_hc)
            
        }
       
catchement_area=[
    ('', 'Z'),
    ('', 'HZ'),
    ('', 'HD'),
]
sex=[
    ('', 'Female'),
    ('', 'Male'),
]
prisonner=[
    ('', 'YES'),
    ('', 'NO'),
]
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = []
        widgets = {
            'district_Name': forms.Select(choices=DISTRICTS),
            'catchement_Area': forms.RadioSelect(choices=catchement_area),
            'sex': forms.RadioSelect(choices=sex),
            'prisonner': forms.RadioSelect(choices=prisonner)
        }
        
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