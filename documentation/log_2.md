# Post-Refactor summary and advice

## Discord conversations

```
Defiler and other viewing eyes, please review my updated classes, now with defiler's advice taken and restructured and all that.
https://github.com/DustinWestGlow/Dustin-chess-game/blob/main/definitions.py
Please also review the tiny project as a whole because I refactored a ton to make it cleaner and with better practices like descriptive variable names.
```

## Plan
Now, I'm asking for some help implementing the functionality. Currently, the game only displays a chess board. I want to be able to do two things.
1. Play a chess game without an AI, just by clicking a bunch.
2. Use a special "replay" mode where moves are made or rewind by using arrow keys.
Both of these features were partially implemented before the refactor.

<br>
Defiler's advice again:
```
- Handle mouse clicks to select (first click) and then move (second click) pieces.
- Validate moves either yourself or using a library like python-chess
- Update the board after each valid move
- Alternate turns between players
- Remember a history of moves
- Add a replay mode that can step through the history
```