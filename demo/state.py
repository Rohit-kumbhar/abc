import reflex as rx  # Reflex framework for creating web applications
import re  # Regular expressions for pattern matching
import hashlib  # Hashing library for password hashing
import os  # OS library for generating salts
from sqlmodel import Field, SQLModel, create_engine, Session, select  # SQLModel for database operations
from sqlmodel import Relationship

from typing import Optional, List


from .structure_user import *      

# This class is used to create the database table for users
class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    full_name: str              #need to check if change of variable name effects used full_name instead of name
    mobile_number: str
    email: str
    password: str
    salt: str
    ## Define a relationship between the User and Workspace classes (one-to-many)
    workspaces: List["Workspace"] = Relationship(back_populates="user") # Define a relationship between the User and Workspace classes (one-to-many)


##########Some Extra classes to make the table-structure#######################

# class User(rx.Model, table=True):   # Define a SQLModel class    #this class is already declared
#     id: Optional[int] = Field(default=None, primary_key=True)   # Define a primary key column
#     name: str
#     email: str
    
    # a user has many workspaces
#   workspaces: List["Workspace"] = Relationship(back_populates="user") # Define a relationship between the User and Workspace classes (one-to-many)

class Workspace(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    
    #a workspace belongs to a user
    user_id: int = Field(foreign_key="user.id") # Define a foreign key relationship between the Workspace and User classes
    user: User = Relationship(back_populates="workspaces") # Define a relationship between the Workspace and User classes (many-to-one)
    
    #a workspace has many projects
    projects: List["Project"] = Relationship(back_populates="workspace") # Define a relationship between the Workspace and Project classes (one-to-many)

class Project(rx.Model, table=True):   # Define a SQLModel class                         
    id: Optional[int] = Field(default=None, primary_key=True) 
    name: str
    # description: Optional[str] = None
    
    #a project belongs to a workspace
    workspace_id: int = Field(foreign_key="workspace.id") # Define a foreign key relationship between the Project and Workspace classes
    workspace: Workspace = Relationship(back_populates="projects") # Define a relationship between the Project and Workspace classes (many-to-one)
   
    #a project has many collections
    collections: List["Collection"] = Relationship(back_populates="project") # Define a relationship between the Project and Collection classes (one-to-many)

class Collection(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    
    #a collection belongs to a project
    project_id: int = Field(foreign_key="project.id")   # Define a foreign key relationship between the Collection and Project classes
   
    project : Project = Relationship(back_populates="collections") # Define a relationship between the Collection and Project classes (many-to-one)
   
    #a collection has many doc_files
    doc_files : List["Doc_file"] = Relationship(back_populates="collection")  

class Doc_file(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    # file_path: str
    # des: Optional[str] = None
    
    #a doc_file belongs to a collection
    collection_id: int = Field(foreign_key="collection.id") # Define a foreign key relationship between the Doc_files and Collection classes
    collection : Collection = Relationship(back_populates="doc_files") # Define a relationship between the Doc_files and Collection classes (many-to-one)
    

# engine = create_engine("sqlite:///database.db", echo=True) # echo=True will print all SQL queries to the terminal
# SQLModel.metadata.create_all(engine)    # Create the database schema for all the SQLModel classes



###############################################################################


# Define the database URL and create the engine
# engine = create_engine("sqlite:///database.db", echo=True)
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, echo=True)

# Create the database tables
SQLModel.metadata.create_all(engine)

# State class for handling application state and user data
class State(rx.State):
    # User details and error messages
    full_name: str = ""
    mobile_number: str = ""
    mobile_error_message: str = ""
    email: str = ""
    email_error_message: str = ""
    password: str = ""
    confirm_password: str = ""
    password_error_message: str = ""
    error_message: str = ""

    # Login details and error messages
    email_log: str = ""
    password_log: str = ""
    error_message_log: str = ""

    # Password reset details and error messages
    email_forget: str = ""
    email_verified: bool = False
    reset_error_message: str = ""

    password_set: str = ""
    confirm_password_set: str = ""
    error_message_set: str = ""
    password_set_error_message: str = ""

    ##storing the current user's email id.
    logged_in_email: str = rx.LocalStorage()   
    ##storing the current user's name.
    #logged_in_name: str = rx.LocalStorage(default="No user")

    # Functions for storing entered details
    def set_full_name(self, value: str):
        self.full_name = value

    def set_mobile_number(self, value: str):
        self.mobile_number = value
        self.validate_mobile_number()

    def set_email(self, value: str):
        self.email = value
        self.validate_email()

    def set_password(self, value: str):
        self.password = value

    # Function to validate the password
    def validate_password(self):
        password_pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
        if not re.match(password_pattern, self.password):
            self.password_error_message = "Password must be at least 8 characters long and contain both letters and numbers."
            return False
        else:
            self.password_error_message = ""
            return True

    # Function to validate the email
    def validate_email(self):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, self.email):
            self.email_error_message = "Invalid email format. Must be sometext@mail.com."
        else:
            self.email_error_message = ""

    # Function to validate the mobile number
    def validate_mobile_number(self):
        if len(self.mobile_number) != 10 or not self.mobile_number.isdigit():
            self.mobile_error_message = "Mobile number must be exactly 10 digits."
        else:
            self.mobile_error_message = ""

    # Function for hashing password
    def hash_password(self, password: str, salt: str) -> str:
        return hashlib.sha256((password + salt).encode('utf-8')).hexdigest()

    # Function to generate a salt
    def generate_salt(self) -> str:
        return os.urandom(16).hex()

    # Function to handle user signup
    def handle_signup_submit(self):
        # Validate mobile number
        self.validate_mobile_number()
        # Validate email format
        self.validate_email()
        # Check if the password meets the criteria
        password_check = self.validate_password()
        
        if password_check:
            # Check if any required field is missing
            if not self.full_name or not self.mobile_number or not self.email or not self.password:
                self.error_message = "Please enter all the details"
                return
            
            # Check if there is an error in the mobile number
            if self.mobile_error_message:
                return
            
            # Generate a salt for password hashing
            salt = self.generate_salt()
            # Hash the password with the generated salt
            hashed_password = self.hash_password(self.password, salt)

            # Start a new database session
            with Session(engine) as session:
                # Create a new User object with the provided details
                new_user = User(
                    full_name=self.full_name,
                    mobile_number=self.mobile_number,
                    email=self.email,
                    password=hashed_password,
                    salt=salt,
                )
                # Add the new user to the database session
                session.add(new_user)
                # Commit the transaction to save the new user in the database
                session.commit()
                # Refresh the session to get the updated user object
                session.refresh(new_user)

            # Set the success message after signup
            self.error_message = "Signup successful!"
            # Retrieve all users to verify the stored data
            self.get_users()
            # Redirect to the login page
            return rx.redirect('/try_login')

    # Function to retrieve all users from the database
    def get_users(self):
        with Session(engine) as session:
            self.users = session.query(User).all()
            for user in self.users:
                print(f"User: {user.full_name}, Email: {user.email}, Mobile: {user.mobile_number},Password: {user.password}")

    # Function to validate the new password
    def validate_password_set(self):
        password_pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
        if not re.match(password_pattern, self.password_set):
            self.password_set_error_message = "Password must be at least 8 characters long and contain both letters and numbers."
            return False
        else:
            self.password_set_error_message = ""
            return True

    # Function to check if the passwords match
    def check_passwords(self):
        if self.validate_password_set():
            if self.password_set != self.confirm_password_set:
                self.error_message_set = "Passwords do not match"
                return False
            else:
                self.error_message_set = ""  # Clear the error message if they match
                return True

    # Function to update the user password
    def update_password(self):
        salt = self.generate_salt()
        hashed_password = self.hash_password(self.password_set, salt)
        with Session(engine) as session:
            statement = select(User).where(User.email == self.email_forget)
            user = session.exec(statement).first()
            if user:
                user.password = hashed_password
                user.salt = salt
                session.add(user)
                session.commit()
                session.refresh(user)
                self.error_message_set = "Password updated successfully!"
            else:
                self.error_message_set = "User not found!"

    # Function to handle password reset submission
    def handle_setpass_submit(self):
        if self.check_passwords():
            if not self.error_message_set:
                self.update_password()
                return rx.redirect('/loginpage')

    # Function to handle user login
    def handle_login_submit(self):
        # Check if the email or password fields are empty
        if not self.email_log or not self.password_log:
            self.error_message_log = "Please enter all the details"
            return

        # Start a new database session
        with Session(engine) as session:
            # Query the database for a user with the provided email
            statement = select(User).where(User.email == self.email_log)
            user = session.exec(statement).first()
            
            # Check if the user exists and the hashed password matches
            if user and self.hash_password(self.password_log, user.salt) == user.password:
                # Set the success message after login
                self.error_message_log = "Login successful!"
                # Store the logged-in user's email
                self.logged_in_email = self.email_log
                self.logged_in_name = user.full_name
                #printing current usser's mail id
                #print(self.logged_in_email)
                rx.console_log("working")
                rx.console_log(self.logged_in_email)
                # Redirect to the logged-in page
                return rx.redirect('/logged_in_page')
            else:
                # Set the error message if the email or password is invalid
                self.error_message_log = "Invalid email or password"


    def handle_logout_click(self):
        # Refresging the logged user mail id
        self.logged_in_email = "No user"
        self.logged_in_name = "No user" 
        #printing current usser's mail id
        #print(self.logged_in_email)
        rx.console_log("working")
        rx.console_log(self.logged_in_email)
        return rx.redirect('/loginpage')
        
    

    # Function to handle email verification for password reset
    def handle_email_verification(self):
        with Session(engine) as session:
            statement = select(User).where(User.email == self.email_forget)
            result = session.exec(statement).first()
            if result:
                self.email_verified = True
                self.reset_error_message = ""
                return rx.redirect('/setpassword')
            else:
                self.email_verified = False
                self.reset_error_message = "Email not found"


    ##########################################################################
    #####These are used for the table-structures##############################


    
    def add_workspace_to_db(self, form_data: dict):
        workspace = Workspace(name=form_data["name"], user_id=form_data["user_id"])
        with rx.session() as session:
            session.add(workspace)
            session.commit()
            #printing the entire table for testing purpose
            users = session.exec(select(Workspace)).all()
            for user in users:
                print(user)

            # session.refresh(self.workspace)
        return rx.toast.info(f"Workspace {form_data['name']} has been added.", variant="outline", position="bottom-right") and rx.redirect('/user_projects')
        
    def add_project_to_db(self, form_data: dict):
        project = Project(name=form_data["name"], workspace_id=form_data["workspace_id"])
        with rx.session() as session:
            session.add(project)
            session.commit()
            #printing the entire table for testing purpose
            users = session.exec(select(Project)).all()
            for user in users:
                print(user)

            # session.refresh(self.Project)
        return rx.toast.info(f"Project {form_data['name']} has been added.", variant="outline", position="bottom-right") and rx.redirect('/user_collections')
    

    def add_collection_to_db(self, form_data: dict):
        collection = Collection(name=form_data["name"],project_id=form_data["project_id"])
        with rx.session() as session:
            session.add(collection)
            session.commit()
            #printing the entire table for testing purpose
            users = session.exec(select(Collection)).all()
            for user in users:
                print(user)
        
            # session.refresh(self.Collection)
        return rx.toast.info(f"Collection {form_data["name"]} has been added.", variant="outline", position="bottom-right") and rx.redirect('/user_docs')
    

    
    def add_doc_file_to_db(self, form_data: dict):
        doc_file = Doc_file(name=form_data["name"], collection_id=form_data["collection_id"])
        with rx.session() as session:
            session.add(doc_file)
            session.commit()
            #printing the entire table for testing purpose
            users = session.exec(select(Doc_file)).all()
            for user in users:
                print(user)

            # session.refresh(self.doc_file)
        return rx.toast.info(f"Document {form_data['name']} has been added.", variant="outline", position="bottom-right")



    ##########################################################################






