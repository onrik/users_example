from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, render
from .forms import User, UserEditForm, SignupForm


def signup_view(request):
    form = SignupForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password2'])
        user.save()

    return render(request, 'signup.html', {'form': form})


@permission_required('is_superuser')
def edit_user_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    form = UserEditForm(request.POST or None, instance=user)

    if request.method == 'POST' and form.is_valid():
        form.save()

    return render(request, 'edit.html', {'form': form})
