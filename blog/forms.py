from django.forms import ModelForm

from blog.models import blog


class BlogForm(ModelForm):
    class Meta:
        # write the name of models for which the form is made
        model = blog

        # Custom fields
        fields = ["title","description"]

    # this function will be used for the validation
    def clean(self):

        # data from the form is fetched using super function
        super(BlogForm, self).clean()

        # extract the username and text field from the data




        # return any errors if found
        return self.cleaned_data