# CSCE Club - Pygame Project

## Introduction
Welcome to UNT CSCE Club's collaborative project! We will take submissions for levels to be added to this framework from *all UNT Students*, regardless of your major, experience, or previous membership in the club. The framework currently supports simple, maze-style games, but you can also turn it into a platformer by adding your own features. Please look at [Level Creation](#level-creation) for more details on our guidelines and recommendations!

If you're new to Python or PyGame, follow our [Setup](#setup) and [Compilation](#compilation) instructions. For further help, take a look at the links in [Resources](#resources).

We're excited to see what kind of fun levels, features, and puzzles you all come up with. We will be playing through all of these levels at our last meeting of the semester, so make sure to join our [discord]( https://discord.gg/cvmvAS85Rv) to get updates about that. Thank you for your interest and contributions!

## Setup


## Compilation
explaining how we are gonna run, explaining how they should test theirs 

## Level Creation
For your reference we have one example level, level1.py, so you can see how this framework is used.
*Your game MUST Start at() and End at()* You can choose to do a plataformer style game or maze style game. Be ware this project is a collaborative effort!
### Sprites
Feel free to add your own sprites (MUST BE APPROPRIATE)
Defining you sprite:
```
sprites = {
    '@': 'sprites/lvl1_player.png',  # Player sprite
    'E': 'sprites/lvl1_enemy.png',   # Enemy sprite
}
```
### Level Design
TBD -> will have to be changed from current
### Collision
Collision is handled for you! Just define walls as '#' -> might have to be changed
```
Code Snippet
```
->from file XXX
### Movement
Would like for players to not have to add this to their level -> any way to include it in one of the config files like main?
## Files Included
├── levels                       # YOUR level file will go here.
│   ├── level1.py                    # Example level file
|   ├── level_transition_example     # Shows the transition between one level to the other (good for testing!)
│   └── lvl_yourinitials.py          # Your level file will go here.
├── sprites                      # YOUR sprite file will go here.
│   ├── lvl1_player.png              # Example level file
│   ├── lvl_yourinitials_player.png  # Your sprites will go here.
├── config.py                        # Contains consts and configuration info. DON'T TOUCH! Talk to us first if you must <3
├── level.py                         # 
├── main.py                          # 
├── minigame_manager.py              # 
└── README.md

### Guidelines
**Recommendations**
// state again where we need to start and end from
// clean
// please submit original work
// don't alter code from framework aside from adding your level and required files
// feel free to use other pygame functions, but use the (specify what they need to use so we don't break others submissions

**What NOT To Do**

### Submissions
- File naming:
    - Level must be named: level_YourInitial.py (we can append the number based on the order we want to add them in) exp. level_MS.py
    - Asset images must be named: <asset>_<YourInitials>.py (replace asset with 'player', 'wall', etc) exp. player_MS.py, wall_MS.py

# Resources
Pygame wiki
