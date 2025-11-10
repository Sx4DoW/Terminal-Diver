import pgzrun

import assets
import classes
from utils.gamestate import GameState
from utils import menu
from pygame import Rect

# Game dimensions
WIDTH = GameState.width
HEIGHT = GameState.height



def draw():
    """Main draw function called by PgZero every frame."""
    if GameState.is_screen(GameState.SCREEN_MAIN_MENU):
        menu.mainMenu.draw(screen)
    elif GameState.is_screen(GameState.SCREEN_SETTINGS):
        menu.settingsMenu.draw(screen)
    elif GameState.is_screen(GameState.SCREEN_GAME):
        # Draw game screen (to be implemented)
        pass

def update(pos):
    """Update function to handle mouse movement on main menu."""
    for gameobject in GameState.game_objects:
        gameobject.update(pos)

def on_mouse_move(pos):
    """Handle mouse movement events."""
    if GameState.is_screen(GameState.SCREEN_MAIN_MENU):
        update(pos)
    elif GameState.is_screen(GameState.SCREEN_SETTINGS):
        menu.settingsMenu.update(pos)

def main():
    """Initialize game and start PgZero."""
    settings_manager = classes.SettingsManager("settings.txt")
    print("Game initialized")
    print("Game started")
    if GameState.current_screen == "quit":
        print("Exiting game...")
        exit(0)



if __name__ == "__main__":
    main()