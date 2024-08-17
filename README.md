**GlassCell**
--------------------------
Welcome to GlassCell, a human-trafficking prevention software. This is a group project for the 2023 AU 24-hour hackathon.

It's called glass cell because the goal is to shed light onto the situation for those who are in a dangerous situation, 
so that the walls of the situation become clear like glass, so someone can help the victim break out of their cell.

To install, download the source code. You must change the DB_PATH variable in DatabaseControl.py to the pathname of your repo’s serverside-data folder.

To run, clone this repo and compile and execute Driver.py. 
See example use cases below the “Driver code” line.

Contributers:
- Angie
- Dan
- Kevin
- Noah

more info: https://www.notion.so/noahflood/GlassCell-3ed94d3d551f4622a5bd52118c897c5d

Pending features (noah's notes)
--------------------------
* Add a way for people to see the public name of the profile/keyword that is not the same
   as the keyword.
* Change the keys database to a more general purpose database (see "datastructures")
* AirDrop support
* Deploy site
* print map to screen on website via online database, make viewable data
* check voice assistant feasability
* chech PHP connection
* glassCell() master function call

Functionality
--------

Database
--------
Every entry ine database contains the following information:
1. Profile:
   Each profile contains a unqiue "keyword," a "screen name" and a history of signals.
2. Signal(s): (-within profiles, same line)
   Each signal has a chronological index in the profile array. Every signal input includes the date & time
   of the signal, the location, the sequential index of the signal, the healthbar of the signal, 
   and the associted message message.

   Abstract Data Structures
   --------------
   1. PROFILES: 
      Stored in a CSV file.
      The CSV file can be parsed using delimeters. 
      For computation and processing, every profile is stored as an item in a dictionary.
      The key is the keyword, the value is embedded lists containing signals.
   ************************************************************************************************************
   ********* To use delimeters, we will need to add flags in the CSV to know when one type of data stops ******
   ********* and another starts.                                                                         ******
   ************************************************************************************************************
   2. SIGNALS:
      Each signal is stored as a linked list? or map? of values to retain order.
   3. DATAPOINTS
      Data points are stored in each signal array as comma-separated values.

In case of generic signals
---------------------------
* Some signals will be entirely empty, with no existing corresponding profile.
* Others may have some subset of fields empty.

Any of the following cases will be overwritten with a new keyword regardless of three possibilites:
   (case A) -- Signal is from an entirely new user.
   (case B) -- Signal is from an existing user who mispelled their keyword.
      In this case, the signal is still broadcast, but the user is notified of the unknown keyword
   (case C) -- Signal is from an existing user who did not specify their keyword for some reason.

* In any of those cases:
   EXPLICIT INFORMATION: 
      Keyword: new one is created
      Healthbar: listed as "unspecified"
      Messsage: a generic message, such as "I'm in danger; I need help!!" is set
   IMPLICIT INFORMATION:
      Screen name: randomly generated
      Location: still stored
      Date/time: still stored and set to new Profile
      Chronological index: set to zero, of course.

Future updates:
-------------------
- Use AI to intelligently smerge profiles with differing keywords
- Prevent spam and snooping by convicts
- provide a way to resolve cases

