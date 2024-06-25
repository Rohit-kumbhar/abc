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



def collections() -> rx.Component:
    # The function definition specifies that it returns a React component.

    return rx.dialog.root(
        # `rx.dialog.root` initializes the dialog component.

        rx.dialog.trigger(
            # `rx.dialog.trigger` defines what triggers the opening of the dialog.

            rx.button(
                # The trigger is a button component.

                rx.icon("plus", size=26),
                # The button contains an icon with a plus sign and a size of 26.

                rx.text("Add Collection", size="4"), 
                # The button also contains text saying "Add Collection" with a size of 4.

                color="primary"
                # The color of the button is set to primary.
            ),
        ),

        rx.dialog.content(
            # `rx.dialog.content` defines the content of the dialog that appears when triggered.

            rx.hstack(
                # `rx.hstack` arranges its children horizontally in a stack.

                rx.badge(
                    # `rx.badge` is a component for displaying a badge.

                    rx.icon(tag="folder", size=34),
                    # The badge contains an icon with a folder tag and a size of 34.

                    radius="full",
                    # The badge is fully rounded.

                    padding="0.65rem",
                    # The badge has a padding of 0.65rem.
                ),

                rx.vstack(
                    # `rx.vstack` arranges its children vertically in a stack.

                    rx.dialog.title("Add Collection",
                        # The title of the dialog is "Add Collection".

                        weight="bold",
                        # The text weight is bold.

                        margin="0",
                        # There is no margin around the title.
                    ),

                    rx.dialog.description(
                        "fill the collection name and project ID",
                        # The description of the dialog instructs to fill in the collection name and project ID.
                    ),

                    spacing="1",
                    # The spacing between the items in the vertical stack is 1.

                    height="100%",
                    # The height of the vertical stack is 100%.

                    align_items="start",
                    # The items in the vertical stack are aligned to the start.
                ),

                height="100%",
                # The height of the horizontal stack is 100%.

                spacing="4",
                # The spacing between the items in the horizontal stack is 4.

                margin_bottom="1.5em",
                # The bottom margin of the horizontal stack is 1.5em.

                align_items="center",
                # The items in the horizontal stack are centered.

                width="100%",
                # The width of the horizontal stack is 100%.
            ),

            rx.flex(
                # `rx.flex` creates a flexible container for the form and buttons.

                rx.form.root(
                    # `rx.form.root` initializes the form component.

                    rx.flex(
                        # `rx.flex` creates a flexible container for form fields.

                        form_field(
                            "Name",
                            "Collection Name",
                            "text",
                            "name",
                            "folder",
                        ),
                        # `form_field` is a custom component for creating form fields.
                        # It creates a text input for "Collection Name".

                        form_field(
                            "Project ID",
                            "Project ID",
                            "number",
                            "project_id",
                            "folder",
                        ),
                        # It creates a number input for "Project ID".

                        direction="column",
                        # The direction of the flexible container is column.

                        spacing="3",
                        # The spacing between the items in the flexible container is 3.
                    ),

                    rx.flex(
                        # Another flexible container for the action buttons.

                        rx.dialog.close(
                            # `rx.dialog.close` creates a button to close the dialog.

                            rx.button(
                                "Cancel",
                                variant="soft",
                                color_scheme="gray",
                            ),
                            # The "Cancel" button has a soft variant and a gray color scheme.
                        ),

                        rx.form.submit(
                            # `rx.form.submit` creates a submit button for the form.

                            rx.dialog.close(
                                rx.button("Add Collection", color="primary"),
                            ),
                            # The "Add Collection" button has a primary color and closes the dialog on submission.

                            as_child=True,
                            # The submit button is a child of the close button.
                        ),

                        padding_top="2em",
                        # The top padding of the flexible container is 2em.

                        spacing="3",
                        # The spacing between the items in the flexible container is 3.

                        mt="4",
                        # The margin top of the flexible container is 4.

                        justify="end",
                        # The items in the flexible container are justified to the end.
                    ),

                    on_submit=State.add_collection_to_db,
                    # The form calls the `add_collection_to_db` method on submission.

                    reset_on_submit=False,
                    # The form does not reset on submission.
                ),

                width="100%",
                # The width of the flexible container is 100%.

                direction="column",
                # The direction of the flexible container is column.

                spacing="4",
                # The spacing between the items in the flexible container is 4.
            ),

            style={"max_width": 450},
            # The maximum width of the dialog content is 450.

            box_shadow="lg",
            # The dialog content has a large box shadow.

            padding="1.5em",
            # The padding of the dialog content is 1.5em.

            border=f"2px solid {rx.color('accent', 7)}",
            # The border of the dialog content is 2px solid with an accent color at the 7th shade.

            border_radius="25px",
            # The border radius of the dialog content is 25px.
        ),
    )

