from django.shortcuts import redirect, render
from .forms import UserForm

users = [
    {
        'name': 'Joao',
        'email': 'joao@gmail.com'
    },
    {
        'name': 'Alice',
        'email': 'alice@gmail.com'
    }
]


def list_users(req):
    context = {
        'users': users
    }
    return render(req, 'list_user.html', context)


def new_user(req):
    userForm = UserForm()
    if req.method == 'POST':
        userForm = UserForm(req.POST)
        if userForm.is_valid():
            user = userForm.cleaned_data
            users.append(user)
            return redirect(list_users)
    context = {
        'form': userForm
    }
    return render(req, 'new_user.html', context)


def edit_user(req, email):
    global users
    user = None
    user_index = 0
    for u in users:
        if u['email'] == email:
            user = u
            break
        user_index += 1

    if not user:
        return redirect(list_users)

    userForm = UserForm(req.POST or None, initial=user)
    if req.method == 'POST':
        if userForm.is_valid():
            user = userForm.cleaned_data
            users[user_index] = user
            return redirect(list_users)

    context = {
        'form': userForm,
        'user': user
    }
    return render(req, 'edit_user.html', context)

def delete_user(req, email):
    global users
    users = [user for user in users if user['email'] != email]
    return redirect(list_users)
