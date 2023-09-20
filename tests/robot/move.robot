*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Move in the middle of the board     0             0             1                     NORTH         0           1           2
Move on the edge of the board       0             0             5                     SOUTH         0           0           6
Bounce left                         0             4             1                     WEST          0           4           2
Bounce down                         4             9             1                     NORTH         4           9           2
Bounce right                        9             2             1                     EAST          9           2           2
Bounce up                           5             0             1                     SOUTH         5           0           2
Move South                          1             2             5                     SOUTH         1           1           6
Move North                          7             7             6                     NORTH         7           8           7
Move EAST                           2             6             10                    EAST          3           6          11
Move WEST                           6             1             4                     WEST          5           1           5

*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}