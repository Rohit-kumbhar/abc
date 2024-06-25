import reflex as rx

from .state import State

# from .structure_user import User_State 



#####this is defining the for########################

def form_field(
    label: str, placeholder: str, type: str, name: str, icon: str, default_value: str = ""
) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.hstack(
                rx.icon(
                    icon, size=16,stroke_width=1.5
                ),
                rx.form.label(label),
                align="center",
                spacing="2",
            ),
            rx.form.control(
                rx.input(
                    placeholder=placeholder,
                    type=type,
                    default_value=default_value,
                ),
                as_child=True,
            ),
            direction="column",
            spacing="1",
            
        ),
        name=name,
        width="100%",
    )

#####################################################



    return rx.flex(
        rx.box(
            "Box 1",
            background_color="lightblue",
            border_radius="3px",
            width="33.33%",
        ),
        rx.box(
            "Box 2",
            background_color="lightgreen",
            border_radius="3px",
            width="33.33%",
        ),
        rx.box(
            "Box 3",
            background_color="lightcoral",
            border_radius="3px",
            width="33.33%",
        ),
        flex_direction="row",
        width="100%",
    )



def add_workspace() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Add Workspace", size="4"), color="primary"
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="folder", size=34),
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.dialog.title("Add Workspace",
                                    weight="bold",
                                    margin="0",
                                    ),
                    rx.dialog.description(
                        "fill the workspace name and user ID",
                    ),
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                margin_bottom="1.5em",
                align_items="center",
                width="100%",
            ),
            rx.flex(
                rx.form.root(
                    rx.flex(
                        form_field(
                            "Name",
                            "Workspace Name",
                            "text",
                            "name",
                            "folder",
                        ),
                        form_field(
                            "User ID",
                            "User ID",
                            "number",
                            "user_id",
                            "folder",
                        ),
                        direction="column",
                        spacing="3",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancel",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button("Add Workspace", color="primary"),
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    on_submit=State.add_workspace_to_db,
                    reset_on_submit=False,
                ),
                width="100%",
                direction="column",
                spacing="4",
            ),
            style={"max_width": 450},
            box_shadow="lg",
            padding="1.5em",
            border=f"2px solid {rx.color('accent', 7)}",
            border_radius="25px",
        ),
    )
    