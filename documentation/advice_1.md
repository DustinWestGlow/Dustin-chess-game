# Chess Game Refactoring

## Phase 1: Low-Hanging Fruit
1. Extract the "replay file" loading into a standalone function (that takes a filename parameter and returns the loaded sequence)
2. Create a "game initialization function" that sets up all the initial game state, even if it's messy for now
3. Extract the "move validation" logic into its own function that takes a piece and positions as parameters

## Phase 2: Reduce Global State
4. Create a simple `GameState` class to hold all the state that's currently stored in globals
5. Refactor handlers to accept a game state parameter instead of relying on globals
6. Move the replay functionality into its own class that manages replay operations

## Phase 3: Separate Game Logic from UI
7. Create a main game loop that clearly separates game updates from rendering
8. Extract the UI rendering code into its own module or class

## Phase 4: Make Input Handling Testable
9. Refactor event handling so each component only handles relevant events
10. Create proper interfaces between components with clear responsibilities

## Benefits:
- Tests can be added at each step
- Codebase improves incrementally
- Game functionality is preserved throughout
- Each refactoring is manageable and focused
- The final result will be fully testable