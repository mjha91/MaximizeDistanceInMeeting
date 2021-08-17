# MaximizeDistanceInMeeting

Purpose: find the spots where participants (or students) sitting in a meeting room will be at the maximum distance from each other
Assumption: participants are sitting in a rectangular room, with no obstructions
Two criteria have been used: first maximizes the minimum distance between the participants; the second maximizes the average distance between participants
The code does take time to run as you increase the number of available positions and participants. As such, I use a random sample if the number of combinations exceeds 100k.


Language Used: Python

