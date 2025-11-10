from typing import Callable, Optional
from pygame import Rect
from pgzero.actor import Actor

from utils.GameObject import GameObject


class Button(GameObject):
    """Button class for interactive clickable buttons.
    Inherits from GameObject and provides functionality for
    drawing, hovering, and clicking.
    """

    def __init__(
        self,
        hitbox: Rect,
        text: str = "",
        text_color: str = "white",
        inactive_color=(50, 50, 50),
        active_color=(100, 100, 100),
        image: Optional[Actor] = None,
        on_click: Optional[Callable[[], None]] = None,
    ):
        """Initialize a button.
        
        Args:
            hitbox: Pygame Rect defining button position and size
            text: Text displayed on the button
            text_color: Color of the button text
            inactive_color: Color when button is not hovered
            active_color: Color when button is hovered
            image: Optional PgZero Actor for button graphics
            on_click: Callable action to invoke on click (optional)
        """
        self.hitbox = hitbox
        self.image = image
        self.text = text
        self.text_color = text_color
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.on_click = on_click

    def is_hovered(self, mouse_pos) -> bool:
        """Check if the button is hovered based on mouse position.
        
        Args:
            mouse_pos: Tuple of (x, y) mouse coordinates
        Returns:
            True if mouse_pos is within button rect, False otherwise
        """
        return self.hitbox.collidepoint(mouse_pos)

    def is_clicked(self, mouse_pos, button) -> bool:
        """Check if the button is clicked based on mouse position.
        
        Args:
            mouse_pos: Tuple of (x, y) mouse coordinates
        Returns:
            True if mouse_pos is within button rect and left mouse button is clicked, False otherwise
        """
        return self.is_hovered() and button == 1

    def update(self, mouse_pos, button=None) -> None:
        """Update button state based on mouse position.
        
        Args:
            mouse_pos: Tuple of (x, y) mouse coordinates
        """
        #print(f"Updating button '{self.text}'")
        if self.is_clicked(mouse_pos, button):
            self.click()

    def click(self) -> None:
        """Invoke the button's click action, if any."""
        if self.on_click:
            self.on_click()
    
    def draw(self, screen) -> None:
        """Draw the button on screen.
        
        Args:
            screen: PgZero screen object
        """
        if not self.hitbox:
            return
        if self.image:
            self.image.draw(screen)
        else:
            # Choose color based on hover state
            color = self.active_color if self.is_hovered else self.inactive_color
            
            # Draw button rectangle
            screen.draw.rect(self.hitbox, color)
            
            # Draw button text centered in the rectangle
            screen.draw.textbox(
                self.text,
                color=self.text_color,
                align="center",
                rect=self.hitbox
            )