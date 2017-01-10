# Donkey Kong



## Functional Specification

This document should become the functional specification of the project you are working on.

A functional specification describes in great detail how a device or program will appear to an
outside user. That is, it treats all hardware as a "black box", the contents of which are completely
unknown to the user. The functional specification should include sections with the following information:

Your specification **should include** the following types of information:


* Summary or introduction. In general, in a few lines or less, what is your program about or what is it about?
    For this project I will make the first level of the clasic game Donkey Kong. The player will have to make his/her way up a 5 level tower using ladders. Barreles will roll down at the player. If the player hits one of these barreles he/she loses a life (you have three lives). Once at the top the player wins the game.

* How does the user access your program? Is it shared via http://runpython.com? Is a web site? Embedded in 
  a single board computer? 
  run python.

* If there are graphics screens involved, describe every screen that the user will experience: what is it for? 
    What did the user have to do to get there and how does she move on to the next?
 There will be three main screens. The start menu. This will be a blank screen with the words "Hit ENTER to start". The next screen will be the play screen. This is the 5 story tower with the player on the bottom and the trophy at the top. The next two screens are very similar. If the player loses all three lives then a screen will display "Game Over" or if the player gets to the top the screen will display "Game Over". 

* For each graphics screen, describe every active control input and what it does. What elements on the screen will
  change in response to user input?
    The first screen will have one control. The enter key will move you into the game. The second screen will have a lot of controls. The player will be able to move left, right, jump and climb up or down ladders. The barreles will not be controled by the player but they will have to roll down the screen.

* Does the program respond to mouse input? What, exactly, does the mouse do?
  There will be no mouse input.

* Does the program respond to keyboard input? How?
  The arrow keys will each be used. The left and right keys will move the player left and right. The up arrow will either make the player jump or climb up ladders. The down arrow will make the player climb down ladders. The ENTER key will also be used. The ENTER key will be used in the first screen to start the game.

* What graphical assets will be used?
 There will be no graphics in this game other than movement.

* Does the user have to do anything to install the program?
  There will be no install.

Your specification should **not** include the following types of information:

* The language you will use to create it.
* Names of any specific files in the project.
* How you will structure the classes, functions and code in your program.
* The name of any files or tools that you will use to design the program.
