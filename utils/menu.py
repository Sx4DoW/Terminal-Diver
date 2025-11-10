"""Menu module for Terminal Quest."""
from typing import Callable, Dict, List, Optional

from utils.Button import Button
from utils import colors
import sys
from utils.gamestate import GameState
from pygame import Rect

WIDTH = GameState.width
HEIGHT = GameState.height

HACKER_PALETTE = colors.HACKER_PALETTE

BUTTON_INACTIVE_COLOR = HACKER_PALETTE[1]
BUTTON_ACTIVE_COLOR = HACKER_PALETTE[0]
TEXT_COLOR = "white"


class Menu:
    """Menu screen class for displaying menus with buttons.

    This class is configurable by passing a title and a list of button
    configurations. An optional callback may be provided to handle
    button clicks.
    """

    def __init__(
        self,
        game_state: GameState,
        title: str,
        buttons: List[Button],
    ) -> None:
        """Initialize a menu.

        Args:
            game_state: GameState object for communication
            title: Title text to display
            buttons: List of Button instances
            on_button_click: Callback function for button clicks (optional)
        """
        self.game_state = game_state
        self.title = title
        self.buttons: List[Button] = buttons

    def draw(self, screen) -> None:
        """Draw the menu screen.

        Args:
            screen: PgZero screen object
        """
        screen.clear()
        screen.fill((10, 10, 10))

        # Draw title
        title = Rect((WIDTH / 16 * 4, HEIGHT / 16 * 1), (WIDTH / 16 * 8, HEIGHT / 16 * 3))
        screen.draw.rect(title, BUTTON_ACTIVE_COLOR)
        screen.draw.textbox(self.title, color="white", align="center", rect=title)

        # Draw buttons
        for button in self.buttons:
            button.draw(screen)
    
    def get_buttons(self) -> List[Button]:
        """Return the list of buttons for this menu.
        
        Returns:
            List of button instances
        """
        return self.buttons

"""Main and settings menu definitions."""

# Main menu buttons: each Button instance owns its on_click behavior.
mainMenu = Menu(
    game_state=GameState,
    title="Terminal Quest",
    buttons=[
        Button(
            rect=Rect((WIDTH / 16 * 5, HEIGHT / 16 * 6), (WIDTH / 16 * 6, HEIGHT / 16 * 2)),
            text="Start Game",
            text_color=TEXT_COLOR,
            inactive_color=BUTTON_INACTIVE_COLOR,
            active_color=BUTTON_ACTIVE_COLOR,
            on_click=lambda: GameState.set_screen(GameState.SCREEN_GAME),
        ),
        Button(
            rect=Rect((WIDTH / 16 * 6, HEIGHT / 16 * 10), (WIDTH / 16 * 4, HEIGHT / 16)),
            text="Settings",
            text_color=TEXT_COLOR,
            inactive_color=BUTTON_INACTIVE_COLOR,
            active_color=BUTTON_ACTIVE_COLOR,
            on_click=lambda: GameState.set_screen(GameState.SCREEN_SETTINGS),
        ),
        Button(
            rect=Rect((WIDTH / 16 * 6, HEIGHT / 16 * 12), (WIDTH / 16 * 4, HEIGHT / 16)),
            text="Quit",
            text_color=TEXT_COLOR,
            inactive_color=BUTTON_INACTIVE_COLOR,
            active_color=BUTTON_ACTIVE_COLOR,
            on_click=lambda: GameState.set_screen(GameState.SCREEN_QUIT),
        ),
    ],
)


# Settings menu (placeholder - add Buttons here as needed)
def on_settings_menu_click(button_index: int) -> None:
    """Handle settings menu button clicks (placeholder)."""
    # TODO: implement actual settings actions
    pass

settingsMenu = Menu(
    game_state=GameState,
    title="Settings",
    buttons=[],
)