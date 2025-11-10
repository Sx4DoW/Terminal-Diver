# Terminal Quest - A Retro-Style Roguelike Adventure

## Project Overview
Terminal Quest is a roguelike game where players explore a computer-themed dungeon using simple terminal commands as abilities. The game features ASCII-style graphics, animated characters, and an engaging soundtrack.

## Technical Requirements

### Approved Libraries
- PgZero (primary game engine)
- math (for calculations)
- random (for enemy movement and item generation)
- pygame.Rect (only this class from Pygame is permitted)

### Game Features

#### Main Menu
- Start Game button
- Toggle Music/Sound button
- Exit button

#### Audio
- Background music for different levels
- Sound effects for:
  - Player movement
  - Command execution
  - Item collection
  - Enemy encounters
  - Level completion

#### Characters

##### Player Character
- Animated idle state (breathing animation)
- Movement animations in four directions
- Command execution animations
- Collision detection with walls and enemies

##### Enemies
- Multiple enemy types with unique behaviors
- Idle animations (various movements)
- Pathfinding movement patterns
- Collision detection with player and environment

#### Game Mechanics
- Grid-based movement system
- Command power-up collection
- Simple inventory system
- Level progression
- Score tracking

### Code Structure

```
terminal_quest/
├── main.py           # Game initialization and main loop
├── assets/           # Game resources
│   ├── images/      # Sprite sheets and graphics
│   ├── sounds/      # Sound effects
│   └── music/       # Background music
├── classes/         # Game classes
│   ├── player.py    # Player character class
│   ├── enemy.py     # Enemy classes
│   ├── level.py     # Level generation and management
│   └── ui.py        # User interface elements
└── utils/          # Utility functions
    ├── animation.py # Animation handling
    └── commands.py  # Game command implementations
```

### Naming Conventions
- Following PEP 8 style guide
- Clear, descriptive names in English
- Example: `player_movement()`, `update_enemy_position()`, `handle_collision()`

### Performance Requirements
- Stable 60 FPS on modern computers
- Quick level loading times
- Smooth character animations
- Responsive controls

## Development Guidelines

### Code Quality
- Implement proper error handling
- Add comments for complex logic
- Keep functions small and focused
- Use type hints for better code readability

### Testing Requirements
- Test all game mechanics thoroughly
- Verify collision detection
- Check animation transitions
- Validate sound system
- Ensure proper game save/load functionality

### Documentation
- Comment all classes and methods
- Provide usage examples
- Document known limitations
- Include setup instructions

## Setup Instructions

1. Ensure Python 3.8+ is installed
2. Install required libraries:
   ```bash
   pip install pgzero
   ```
3. Run the game:
   ```bash
   python main.py
   ```

## Controls
- Arrow keys: Move character
- Space: Execute command
- E: Open inventory
- ESC: Pause menu

## Credits
All assets, code, and game design are original work created specifically for this project.
