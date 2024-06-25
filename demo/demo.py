"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from .navbar import navbar
from .login_navbar import login_navbar
from .loginbox import logina
from .loginbox_navbar import home
from .forget_pass import forgetbox
from .setpass_box import setbox
from .footer import footer
from .signup_box import sign_up
from .logged_in import logged_in_box
from .logged_in_navbar import logged_navbar
from .try_login import post_signin
from .user_mail import check_user_mail
# from .structure_user import User_State
# from .structure_user import *            #here all the structure and hirarcy are defined
from .user_collections import collections
from .user_workspaces import add_workspace
from .user_projects import add_project
from .user_docs import add_doc_file


from .state import State

from rxconfig import config







def index():
    return rx.container(
       
        navbar(),
        rx.divider(height='35px', style={"background-color": "white"}),
        home(),
        footer(),
    )

def login():
    return rx.container(
        navbar(),
        rx.divider(height='35px', style={"background-color": "white"}),
        logina(),
        footer(),

    )


def sign_up_page():
    return rx.container(
        navbar(),
        rx.divider(height='35px', style={"background-color": "white"}),
        sign_up(),
        footer(),

    )

def forget_pass():
    return rx.container(
        navbar(),
        rx.divider(height='35px', style={"background-color": "white"}),
        forgetbox(),
        footer(),

    )


def set_pass():
    return rx.container(
        navbar(),
        rx.divider(height='35px', style={"background-color": "white"}),
        setbox(),
        footer(),

    )

def logged_in():
    return rx.container(
        logged_navbar(),
        rx.divider(height='35px', style={"background-color": "white"}),
        logged_in_box(),
        footer(),

    )


def try_to_login():
    return rx.container(
        navbar(),
        rx.divider(height='35px', style={"background-color": "white"}),
        post_signin(),
        footer(),

    )



def check_user():
    return rx.container(
        navbar(),
        rx.divider(height='35px', style={"background-color": "white"}),
        check_user_mail(),
        footer(),

    )



def user_workspaces():
    return rx.container(
        navbar(),
        rx.divider(height='35px', style={"background-color": "white"}),
        add_workspace(),
        footer(),

    )

def user_projects():
    return rx.container(
        navbar(),
        rx.divider(height='35px', style={"background-color": "white"}),
        add_project(),
        footer(),

    )


def user_collections():
    return rx.container(
        navbar(),
        rx.divider(height='35px', style={"background-color": "white"}),
        collections(),
        footer(),

    )


def user_docs():
    return rx.container(
        navbar(),
        rx.divider(height='35px', style={"background-color": "white"}),
        add_doc_file(),
        footer(),

    )



app = rx.App()
app.add_page(index)
app.add_page(login,route='/loginpage')
app.add_page(forget_pass,route='/forgetpass')
app.add_page(set_pass,route='/setpassword')
app.add_page(sign_up_page,route='/sign_up_page')
app.add_page(logged_in,route='/logged_in_page')
app.add_page(try_to_login,route='/try_login')
app.add_page(check_user,route='/check_user')
app.add_page(user_collections,route='/user_collections')
app.add_page(user_workspaces,route='/user_workspaces')
app.add_page(user_projects,route='/user_projects')
app.add_page(user_docs,route='/user_docs')

######## Add API routes######################################################################

# app.api.add_api_route("/users/{user_id}/workspaces", User_State.get_user_workspaces)
# app.api.add_api_route("/workspaces/{workspace_id}/projects", User_State.get_workspace_projects)
# app.api.add_api_route("/collections/{collection_id}/files", User_State.get_project_collections)
# app.api.add_api_route("/projects/{project_id}/collections", User_State.get_collections_files)
# app.api.add_api_route("/files/{file_id}", User_State.get_files)


# @rx.api_route("/collections/{collection_id}/files", methods=["GET"])
# @rx.api_route("/projects/{project_id}/collections", methods=["GET"])
# @rx.api_route("/files/{file_id}", methods=["GET"])

##############################################################################

app._compile()
