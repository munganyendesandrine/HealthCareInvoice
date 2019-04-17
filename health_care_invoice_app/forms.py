from django import forms
from .models import HealthPost,Patient,ServiceDetails,WelcomeMsgRecipients

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
            'catchement_Area': forms.RadioSelect(choices=catchement_area),
            'sex': forms.RadioSelect(choices=sex),
            'prisonner': forms.RadioSelect(choices=prisonner)
        }
type_Of_Medical_Visit=[
    ('', 'Outpatient'),
    ('', 'Inpatient'),
] 
desease_Episode=[
    ('', 'New Case'),
    ('', 'Old Case'),
]     
purpose_Of_The_Visit=[
    ('', 'Natural Disease'),
    ('', 'Occupational Disease'),
    ('', 'Road Traffic Accident'),
    ('', 'Work Accident'),
    ('', 'Other'),
]
consultation=[
    ('', 'Description'),
    ('', 'Quantity/Days'),
    ('', 'Unit Cost'),
    ('', 'Total Cost'),
]
class ServiceDetailsForm(forms.ModelForm):
    class Meta:
        model = ServiceDetails
        exclude = []
        widgets = {
            'type_Of_Medical_Visit': forms.RadioSelect(choices=type_Of_Medical_Visit),
            'desease_Episode': forms.RadioSelect(choices=desease_Episode),
            'purpose_Of_The_Visit': forms.RadioSelect(choices=purpose_Of_The_Visit),
            'consultation': forms.RadioSelect(choices=consultation),
        }

class HealthPostForm2(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')