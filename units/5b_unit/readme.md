# Bonus Unit: Serving Up Python Web Apps #

The general idea is that we can use a python library called [web.py](http://webpy.org/) to serve up web page data.  Cloud 9 stores our programs in the cloud and when we run a program that uses the [web.py](http://webpy.org/) library, it will serve webpages at an address we can access at a location like:
https://<your id>.c9users.io/

### Important notes: ###
1.  You will need to use python 2 to use web.py (we have been using python 3 for the rest of the semester).  Make sure to change it before trying to run a program in this unit.  

And remember to change it back to python 3 before moving onto the next unit!
2.  many parts to a web page
	html - is the markup language that says where to put text, boxes, colors, fonts, images, etc
	javascript - is what you need to make a page dynamic so that you can iteract with it
		(push a button, make something happen, type in something, have the page respond)
	python - in this case we're using python as the "backend" language.  that means it will do the work on
		the server and send data to the browser
		we'll be using a python library called web.py that will help us generate the html.
		 since we already have some python programs, we will try to adapt it into a web app.
3.  what is the simplest program you can write in any language?  Hello World.
	- here's what hello world looks like as a python web app (see webapp_01.py)
	- here's how you get it to work
		- run this in cloud9, see the terminal and it will tell you the app is running at a url like:  https://smhs-01tingting-ttwu.c9users.io
		- now you can paste this url into a browser of your choice (chrome, firefox, etc)
	- go through the different required parts of the webapp
	- here's what it looks like when you have a python error
		- step 1 still runs
		- but when you try to access the page, you will get the error
4.  
	- what if you wanted it to say something else other than "Hello World?"
	- what if you wanted some other page to do something else?  like if I wanted 'https://smhs-01tingting-ttwu.c9users.io/bunny' to give me a bunny 

ascii art?

5.      
    what if you want to make a web app that printed out the patterns from your lab 4.3?
	make it so that if you go to the link
	"https://<your id>.c9users.io/b7_stars" it prints
	"https://<your id>.c9users.io/stars_and_stripes" it prints
	...

6.  how do you do inputs?

7.  how do you add html tags?
	