# CSCE Club - Pygame Project

## Introduction
Welcome to UNT CSCE Club's collaborative project! We will take submissions for levels to be added to this framework from *all UNT Students*, regardless of your major, experience, or previous membership in the club. The framework currently supports simple, maze-style games, but you can also turn it into a platformer by adding your own features. Please look at [Level Creation](#level-creation) for more details on our guidelines and recommendations!

If you're new to Python or PyGame, follow our [Setup](#setup) and [Compilation](#compilation) instructions. For further help, take a look at the links in [Resources](#resources).

We're excited to see what kind of fun levels, features, and puzzles you all come up with. We will be playing through all of these levels at our last meeting of the semester, so make sure to join our [discord]( https://discord.gg/cvmvAS85Rv) to get updates about that. Thank you for your interest and contributions!

## Setup


## Compilation
explaining how we are gonna run, explaining how they should test theirs 

## Level Creation
For your reference we have one example level, level1.py, so you can see how this framework is used. *Your game MUST Start at() and End at()*

You can choose to do a platformer or maze-style game. However, please keep in mind that this project is a collaborative effort, and do not change anything outside of your level file. If you find that your idea requires you to modify any of the other files, please consult one of our officers!

### Sprites
Feel free to add your own sprites, but make sure they are **appropriate**. Anything violating UNT's [Code of Student Conduct](https://policy.unt.edu/policy/07-012) will result in your level being thrown out.

**Defining Your Sprite:**
First, upload your sprites to the sprites folder in the provided framework. Then, using the below code as an example, replace 'lvl1_player.png' with the sprite file name.
```
sprites = {
    '@': 'sprites/lvl1_player.png',  # Player sprite
    'E': 'sprites/lvl1_enemy.png',   # Enemy sprite
}
```
### Level Design
TBD -> will have to be changed from current

### Collision
Collision is handled for you! Just define walls as '#' and the enemy as 'E'. -> might have to be changed

Below is the maze included in our level1.py file. You can use this as a reference as you build your level!
```
layout = [
    "#"*(MAZE_WIDTH+1),
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "# ###"+" "*(MAZE_WIDTH-5)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "# "+" "*(MAZE_WIDTH-7)+"######",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"*(MAZE_WIDTH)+"#",
]
```
### Movement
Would like for players to not have to add this to their level -> any way to include it in one of the config files like main?

## Files Included
```
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
```

### Guidelines
We ask that you thoroughly read these guidelines before submission to ensure that your submission meets everything listed below. Depending on when you submit, we may not be able to give you time to fix your submission, and we would hate for it to be left out! If you have any doubts on whether your modifications are okay, ***please ask an officer*** via Discord, Instagram, or E-mail.

- As mentioned in the previous sections, your level must *start at () and end at ()*.
- Make sure your code is clean and readable (don't leave in any commented-out sections, stick to one method of formatting, etc.)
- Do not submit work that isn't your own. Using external resources as a guide to help you create what you're envisioning is completely okay, but blatant copying will not be tolerated.
- Do not alter any code outside of your custom level file. It's encouraged to upload and use your own sprites, too, but make sure those files stay in the right folders!
  - Feel free to use other pygame functions, too, but make sure it stays in your file.

Once again, if you need clarification on what you can or can't do, please reach out to us! We want everyone to be as involved as possible.

### Submissions
- File naming:
    - Level must be named: level_YourInitial.py
        - If you're submitting multiple levels, append a number based on the order you would like them to be played.
        - E.g.: Jane Doe would submit level_JD.py for only one submission. For two, she would submit level_JD1.py and level_JD2.py, where level_JD1.py is played first.
    - Asset images must be named: <asset>_<YourInitials>.py, where <asset> describes what the sprite is used for (player, wall, etc.)
        - Again, Jane Doe would have assets player_JD.py, wall_JD.py, and enempy_JD.py
        - These are optional! If you would like to use our default sprites, just don't upload any images.

# Resources
Here are some helpful resources you can reference while building your level!

= [PyGame Wiki](https://www.pygame.org/docs/)
