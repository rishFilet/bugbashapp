from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileForm
from bugbashapp.firebase import FirebaseDB


def signUp(request):
    return render(request, "signUp.html")


def postSignup(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            try:
                userDB = FirebaseDB().authe.create_user_with_email_and_password(user.email,
                                                                               user.password)
                uid = userDB['localId']
                data = {"First": user.data.get('first_name'), "Last": user.data.get(
                    'last_name'),
                        "Email": user.email, "Role": profile_form.data.get('role')}
                FirebaseDB().database.child("users").child(uid).set(data)
            except:
                message = "Unable to create account try again"
                return render(request, "signup.html", {"messg": message})
            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Now we save the UserProfile model instance.
            profile.save()
            registered = True

            #return render(request,'signIn.html', )
            #database.child("users").child(uid).child("details").set(data)
            # Update our variable to tell the template registration was successful.

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request, 'signUp.html')
#'user_form': user_form, 'profile_form': profile_form, 'registered': registered}