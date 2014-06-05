from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
            max_length=200,
            widget=forms.TextInput(attrs={
                'class':'pure-input-1',
                'placeholder':'Full Name',
                'type': 'text',
                })
            )
   #company = forms.CharField(
   #         widget=forms.TextInput(attrs={
   #             'placeholder':'Company',
   #             'type':'text',
   #             })
   #         )
   # title = forms.CharField(
   #         widget= forms.TextInput(
   #             attrs={
   #                 'placeholder':'Title',
   #                 'type':'text',
   #                 'class':'pure-input-1',
   #             })
   #         )
   # phone_number = forms.CharField(
   #         widget= forms.TextInput(
   #             attrs={
   #                 'placeholder':'Phone Number',
   #                 'type':'text',
   #                 })
   #         )
    email =  forms.EmailField(
            widget= forms.TextInput(
                attrs={
                    'class':'pure-input-1',
                    'placeholder':'Email',
                    'type':'Email',
                })
            )
    message = forms.CharField(required=False,
            widget=forms.Textarea(
                attrs={
                    'class':'pure-input-1',
                    'placeholder':'description',
                    'type':'text',
                }
            )
        )


