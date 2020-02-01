# Concord on Discord

Concord on Discord is a discord server born of an attempt to create a viable bible study for those who could benefit from the touch-and-go nature of a modern chat app in their attempt to study the bible. Shut-ins, youth, busy parents, those with jobs with odd schedules, anyone whose time is at a premium or presence is difficult to acheive, and anyone looking to chat with like-minded people are all possible users.

## Usage

This repository is a bot and it's files written in python. This bot is built around the following discord server structure:

#### Concord on Discord
- welcome
    - lobby
    - course-catalog
- studies
    - study chat
    - study notes

and there are three permission levels: masses, student, and teacher. 

The general concept is that anyone can join with an unlimited join link. They are given masses permissions. All they see is the lobby and the course-catalog. Usher acts as a greeter/bouncer for the lobby. Usher steers people to the course-catalog where they can then deal with Dean.

Dean keeps track of students and teachers and studies. If an application is accepted by Dean from one of the masses, they are granted student permissions, and they can enter the bible study they applied for. Dean will also deal with teachers in setting up studies. Studies are created with an agreed upon deletion date.

Luther recites ESV bible verses and Book of Concord passages.

Lawrence sweeps the lobby and performs other menial tasks.

## Attribution
Our List of Dirty, Naughty, Obscene, and Otherwise Bad Words © 2012–2019 Shutterstock, Inc. https://creativecommons.org/licenses/by/4.0/

Unless otherwise indicated, all Scripture quotations are from the ESV® Bible (The Holy Bible, English Standard Version®), copyright © 2001 by Crossway, a publishing ministry of Good News Publishers. Used by permission. All rights reserved. You may not copy or download more than 500 consecutive verses of the ESV Bible or more than one half of any book of the ESV Bible.

## Required Packages
```python
import discord
import requests
import dotenv
import tinydb
```

## License
[BSD-3-Clause](https://github.com/cartwright/CoD/blob/master/bsd3clause_license)
