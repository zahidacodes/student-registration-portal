from django import forms

class myform(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    branch = forms.CharField(max_length=100)
    ph_number = forms.IntegerField()

    # def clean_name(self):
    #     vname = self.cleaned_data["name"]
    #     if len(vname) < 4 :
    #         raise forms.ValidationError("Enter more than 4 character")
    #     return vname
   
