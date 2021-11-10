# Konane
## Two-player strategy board game from Hawaii

This is an implementation of a minimax adversarial search algorithm with alpha-beta
pruning on the game of Konane, also known as Hawaiian Checkers. The game is played
on an N by N board of black and white pieces. N may be as small as 4 or as large as 8.
The board uses **'B'** for black pieces and **'W'** for white pieces.

## Game Description

In order to play Konane, the black player goes first and removes one black piece from the
corner or the center of the board. For an 8 by 8 board, this equates to positions (0,0),
(3,3), (4,4), or (7,7). Next the white player removes a white piece adjacent to the space
created by the first move. Then the players alternate moves, each jumping one of their
own pieces over one horizontally or vertically adjacent opponent's piece, landing in an
empty space on the other side, and removing the jumped piece. If desired, this may be
continued in a multiple jump, as long as the same piece is moved in a straight line. The
game ends when one player can no longer move and that player is considered the loser. 
