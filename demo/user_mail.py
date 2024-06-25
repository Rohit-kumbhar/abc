import reflex as rx
from .state import State





def check_user_mail():
    return rx.hstack(
    rx.flex(
 
                rx.hstack(
                 
                        rx.box(
                          rx.heading(
                              "The current user is: ",
                              size="7",  # Adjust size as needed
                              weight="bold",  # Make the text bold
                              margin_bottom="22px", # Add 100px space below this heading
                              #width="40%",
                              align_items="top",
                          ),
                          rx.text(State.logged_in_email,
                            color="red",
                            size="4",
                            weight="medium",
                            text_align="left",
                            width="100%",
                                ),
                    
                        width="100%",
                          
                        ),
                ),

    ),

    )

