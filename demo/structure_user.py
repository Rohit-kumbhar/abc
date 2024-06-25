# import reflex as rx  # Reflex framework for creating web applications
# import re  # Regular expressions for pattern matching
# import hashlib  # Hashing library for password hashing
# import os  # OS library for generating salts

# from sqlmodel import Field, SQLModel, create_engine, Session, select  # SQLModel for database operations

# from sqlmodel import Relationship


# # Define the database URL and create the engine
# DATABASE_URL = "sqlite:///./test.db"
# engine = create_engine(DATABASE_URL)


####################################################



# class App_User(SQLModel, table=True):
#     id: int = Field(default=None, primary_key=True)
#     workspaces: list["Workspace"] = Relationship(back_populates="user")

# class Workspace(SQLModel, table=True):
#     id: int = Field(default=None, primary_key=True)
#     user_id: int = Field(default=None, foreign_key="app_user.id")
#     user: App_User = Relationship(back_populates="workspaces")
#     projects: list["Project"] = Relationship(back_populates="workspace")

# class Project(SQLModel, table=True):
#     id: int = Field(default=None, primary_key=True)
#     workspace_id: int = Field(default=None, foreign_key="workspace.id")
#     workspace: Workspace = Relationship(back_populates="projects")
#     collections: list["Collection"] = Relationship(back_populates="project")

# class Collection(SQLModel, table=True):
#     id: int = Field(default=None, primary_key=True)
#     project_id: int = Field(default=None, foreign_key="project.id")
#     project: Project = Relationship(back_populates="collections")
#     files: list["File"] = Relationship(back_populates="collection")

# class File(SQLModel, table=True):
#     id: int = Field(default=None, primary_key=True)
#     collection_id: int = Field(default=None, foreign_key="collection.id")
#     collection: Collection = Relationship(back_populates="files")



# class User_State(rx.State):

#     #@rx.api_route("/users/{user_id}/workspaces", methods=["GET"])
#     async def get_user_workspaces(user_id: int):
#         with Session(engine) as session:
#             user = session.exec(select(App_User).where(App_User.id == user_id)).first()
#             return rx.json(user.dict())

#     # Define API route for fetching workspace projects
#     #@rx.api_route("/workspaces/{workspace_id}/projects", methods=["GET"])
#     async def get_workspace_projects(workspace_id: int):
#         with Session(engine) as session:
#             workspace = session.exec(select(Workspace).where(Workspace.id == workspace_id)).first()
#             return rx.json(workspace.dict())

#     # Define API route for fetching project collections
#     #@rx.api_route("/projects/{project_id}/collections", methods=["GET"])
#     async def get_project_collections(project_id: int):
#         with Session(engine) as session:
#             project = session.exec(select(Project).where(Project.id == project_id)).first()
#             return rx.json(project.dict())

#     # Define API route for fetching collection files
#     #@rx.api_route("/collections/{collection_id}/files", methods=["GET"])
#     async def get_collections_files(collection_id: int):
#         with Session(engine) as session:
#             collection = session.exec(select(Collection).where(Collection.id == collection_id)).first()
#             return rx.json(collection.dict())

#     # Define API route for fetching a file
#     #@rx.api_route("/files/{file_id}", methods=["GET"])
#     async def get_files(file_id: int):
#         with Session(engine) as session:
#             file = session.exec(select(File).where(File.id == file_id)).first()
#             return rx.json(file.dict())



    ################################################################################################


    # def create_workspace(self):
    #         new_workspace = Workspace(user_id=self.logged_in_email)  # Create new workspace for the user
    #         with Session(engine) as session:
    #             session.add(new_workspace)  # Add new workspace to the session
    #             session.commit()  # Commit the transaction to save the workspace to the database
    #             return rx.text(f"Workspace created with ID: {new_workspace.id}")  # Display confirmation
    ################################################################################################

    # # Add API routes
    # app.add_api_route("/users/{user_id}/workspaces", get_user_workspaces)
    # app.add_api_route("/workspaces/{workspace_id}/projects", get_workspace_projects)