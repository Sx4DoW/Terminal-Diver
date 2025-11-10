"""Game state module for Terminal Quest.

This module exposes a class-based (static) GameState. The class uses
class attributes to store application-wide state so it behaves like a
static container.
"""

from typing import List


class GameState:
    """Static-like container for global game state.

    All attributes are class attributes and therefore shared across the
    application. Use the provided classmethods for controlled updates
    when side-effects or validation are required.
    """

    # Valid screen identifiers
    SCREEN_MAIN_MENU: str = "Main Menu"
    SCREEN_SETTINGS: str = "Settings"
    SCREEN_GAME: str = "Game"
    SCREEN_QUIT: str = "Quit"

    # Display dimensions
    width: int = 800
    height: int = 600

    # Current screen identifier
    current_screen: str = SCREEN_MAIN_MENU

    # List of drawable game objects
    game_objects: List[object] = []

    @classmethod
    def set_screen(cls, name: str) -> None:
        """Change the current screen with validation.

        Args:
            name: Screen identifier (use SCREEN_* class constants)

        Raises:
            ValueError: If screen name is not valid
        """
        valid_screens = (cls.SCREEN_MAIN_MENU, cls.SCREEN_SETTINGS, cls.SCREEN_GAME)
        if name not in valid_screens:
            raise ValueError(f"Invalid screen: {name}. Must be one of {valid_screens}")
        cls.current_screen = name

    @classmethod
    def is_screen(cls, name: str) -> bool:
        """Check if the current screen matches the given name.

        Args:
            name: Screen identifier to check

        Returns:
            True if current_screen matches name, False otherwise
        """
        return cls.current_screen == name