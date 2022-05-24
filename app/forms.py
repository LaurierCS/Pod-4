from django import forms
from django.forms import ModelForm, TextInput, EmailInput, DateTimeInput, ClearableFileInput, URLInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import *

class ExperienceInputform(forms.ModelForm): 
    name = forms.CharField(required=True)
    # type = forms.ModelMultipleChoiceField(
    #   queryset=Experience.EXPERIENCE_TYPE, 
    #   )
    # start as text input and adjust to match figma
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.filter(node_type="N"),
        required=True,
        label="Skills", 
        help_text="What Skills did you learn or use?"
    )
    kind = forms.ChoiceField(choices=Experience.EXPERIENCE_TYPE)
    description = forms.Textarea()
    start_date = forms.DateField(widget=forms.SelectDateWidget)
    end_date = forms.DateField(widget=forms.SelectDateWidget)
    project_link = forms.URLInput()
    image = forms.ImageField(required=False)
    
    class Meta:
        model = Experience
        fields = "__all__"
        exclude = ('profile', 'likes_amount',)

        # lables = { 
        #   "name": "Experience Name",
        #   "markers": "Add Marker Tags",
        #   "kind": "Experience Type",
        #   "descripton": "Experience Description",
        # }

    def __init__(self, *args, **kwargs):
      super(ExperienceInputform, self).__init__(*args, **kwargs)
      self.fields['name'].widget.attrs.update({'class': 'input'})
      self.fields['skills'].widget.attrs.update({'class': 'input multi-select-input'})
      self.fields['description'].widget.attrs.update({'class': 'input fixed-size-input'})
      self.fields['start_date'].widget.attrs.update({'class': 'input select'})
      self.fields['end_date'].widget.attrs.update({'class': 'input select'})
      self.fields['project_link'].widget.attrs.update({'class': 'input'})
      self.fields['kind'].widget.attrs.update({'class': 'input select'})
      self.fields['image'].widget.attrs.update({'class': 'tech-tag tech-tag-blue'})

    def clean(self):
      cleaned_data = super().clean()
      start_date = cleaned_data.get("start_date")
      end_date = cleaned_data.get("end_date")
      if end_date and end_date < start_date:
        raise forms.ValidationError(("End date should be greater than start date."), code="invalidDate")
      return cleaned_data


# class customMMCF():

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username','email', 'password1', 'password2', 'first_name', 'last_name']

class UserSettingForm(ModelForm):
  class Meta:
    model = Profile
    fields = '__all__'
    exclude = ['user', 'date_created']

  first_name = forms.CharField(
    label='first name',
    widget=forms.TextInput(
      attrs={
        'class': 'input my-4 px-3 placeholder-gray-500 invalid:border-pink-500 invalid:text-pink-600 focus:invalid:border-pink-500 focus:invalid:ring-pink-500',
        'placeholder': 'Write your first name here...',
        },
      ),
    )
  last_name = forms.CharField(
    label='last name',
    widget=forms.TextInput(
      attrs={
        'class': 'input my-4 px-3 placeholder-gray-500 invalid:border-pink-500 invalid:text-pink-600 focus:invalid:border-pink-500 focus:invalid:ring-pink-500',
        'placeholder': 'Write your last name here...',
        }
      ),
    )
  email = forms.EmailField(
    label='email address',
    widget=forms.EmailInput(
      attrs={
        'class': 'input my-4 px-3 placeholder-gray-500 invalid:border-pink-500 invalid:text-pink-600 focus:invalid:border-pink-500 focus:invalid:ring-pink-500',
        'placeholder': 'Write your email here...'
        }
      ), 
      required=False,
    )
  twitter = forms.URLField(
    label='twitter',
    widget=forms.URLInput(
      attrs={
        'class': 'input my-4 px-3 placeholder-gray-500 invalid:border-pink-500 invalid:text-pink-600 focus:invalid:border-pink-500 focus:invalid:ring-pink-500',
        'placeholder': 'https://twitter.com/<username>'
      },
    ),
     required=False,
  )
  linkedin = forms.URLField(
    label='linkedin',
    widget=forms.URLInput(
      attrs={
        'class': 'input my-4 px-3 placeholder-gray-500 invalid:border-pink-500 invalid:text-pink-600 focus:invalid:border-pink-500 focus:invalid:ring-pink-500',
        'placeholder': 'https://www.linkedin.com/in/<username>'
      }
    ),
    required=False,
  )
  github = forms.URLField(
    label='github',
    widget=forms.URLInput(
      attrs={
        'class': 'input my-4 px-3 placeholder-gray-500 invalid:border-pink-500 invalid:text-pink-600 focus:invalid:border-pink-500 focus:invalid:ring-pink-500',
        'placeholder': 'https://github.com/<username>'
      }
    ),
    required=False,
  )
  website = forms.URLField(
    label='website',
    widget=forms.URLInput(
      attrs={
        'class': 'input my-4 px-3 placeholder-gray-500 invalid:border-pink-500 invalid:text-pink-600 focus:invalid:border-pink-500 focus:invalid:ring-pink-500',
        'placeholder': 'Place your own website url here...'
      }
    ),
    required=False,
  )
  image = forms.ImageField(
    label='Upload image',
    widget=forms.ClearableFileInput(),required=False,
  )
  bio = forms.CharField(
    label='Biography',
    widget=forms.Textarea(
      attrs={
        'class':'input bg-transparent border-2 rounded-xl overflow-hidden min-h-[100px] my-4 px-3 resize-none box-bordere w-full placeholder-gray-500 invalid:border-pink-500 invalid:text-pink-600 focus:invalid:border-pink-500 focus:invalid:ring-pink-500',
        'rows': '4',
        'placeholder': 'Boast about yourself😎'
        }),
        required = False,
    )


class SearchQueryForm(forms.Form):
  search_query = forms.CharField(required=True)
  search_scope = forms.CharField(required=True)

