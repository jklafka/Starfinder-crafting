# Starfinder crafting table

The Starfinder crafting interface offered through Roll20 is clunky and difficult work with, while the crafting system itself is fun.

This project uses Python3 and Flask on the backend and TypeScript React on the fronted.

## Model notes

Create component crafting costs for each item
PCs choose item
https://developers.google.com/sheets/api/

Generate tests (which type, order)
Pseudo-random number generator (https://en.wikipedia.org/wiki/Linear_congruential_generator)
First test is just max of fabrication weights
Then iteratively generate next entry by random number generator
Then go down the list of MCPRB and decrement by the costs in those places
When it goes negative then that’s the test
No sequential repeats

Jumping
Can’t go more than 3 without jumping [hard constraint]
Rarely jumps 0
Usually jumps 1
Rarely jumps 2
Potentially
[Gaussians]
 PCs allocate to tests (can’t do two tests at once but can be sequential)
Roll to see if passes
