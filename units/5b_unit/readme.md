# Bonus Unit: Serving Up Python Web Apps #

The general idea is that we can use a python library called [web.py](http://webpy.org/) to serve up web page data.  Cloud 9 stores our programs in the cloud and when we run a program that uses the [web.py](http://webpy.org/) library, it will serve webpages at an address we can access at a location like:
https://\<your id>\.c9users.io/

### Important notes: ###
1.  __You will need to use python 2__ to use web.py (we have been using python 3 for the rest of the semester).  Make sure to change it before trying to run a program in this unit.
(To change it, go to settings for your workspace
![settings](https://github.com/ttwu/2nd-semester-introduction-to-computer-science-principles/blob/master/units/5b_unit/webapp01.PNG?raw=true "settings")
then scroll to the bottom and change the Python setting.)
And remember to change it back to python 3 before moving onto the next unit!
2.  __There are many parts to a web page.__
    * __HTML__ - is the markup language that says where to put text, boxes, colors, fonts, images, etc.
	* __javascript__ - is the language that makes a page dynamic so that you can iteract with it (push a button, make something happen on the page, type in something, have the page respond).
	* Both HTML and javascript are what are called front-end languages.  They're the data that gets sent to the internet browser and interpreted into a visual webpage for you.
	* __python__ - in this case we're using python as the "backend" language.  That means it will get run on the Cloud9 server and figure out what HTML and javascript code it will send to the browser.  Let's try adapting some of our python programs into web apps!

### Let's get started! ###
1.  __What is the simplest program you can write in any language?__ Hello World.
	- Here's what hello world looks like as a python web app.  Type it up and save as webapp01.py in a new folder in your workspace called __webapps__.
	![hello world](https://github.com/ttwu/2nd-semester-introduction-to-computer-science-principles/blob/master/units/5b_unit/webapp02.PNG?raw=true)
	- __Here's how you get it to serve up as a webpage.__
		- Run this in cloud9.  ![run](https://github.com/ttwu/2nd-semester-introduction-to-computer-science-principles/blob/master/units/5b_unit/webapp03.PNG?raw=true)
		- Look at the terminal and it will tell you the app is running at a url like:  https://\<your_cloud9_account_name>\.c9users.io
	    ![link](https://github.com/ttwu/2nd-semester-introduction-to-computer-science-principles/blob/master/units/5b_unit/webapp04.PNG?raw=true)
		- Now you can paste this url into a browser of your choice (chrome, firefox, etc) and you should see
		![link](https://github.com/ttwu/2nd-semester-introduction-to-computer-science-principles/blob/master/units/5b_unit/webapp05.PNG?raw=true)
    - Also note that after you loaded the page, in your cloud9 terminal, it will show:
    ![log](https://github.com/ttwu/2nd-semester-introduction-to-computer-science-principles/blob/master/units/5b_unit/webapp06.PNG?raw=true)
    That shows that our server code got a reqest for the "/" page and it successfully responded.

### What's happening here? ###
1.  Look over the comments in the code. __Each major parts of the webapp__ is numbered.
2.  __When you first run your program in Cloud 9,__
    - web is imported
    - urls variable gets created (with a mapping of the page https://\<your id>\.c9users.io/ to helloWorldApp class)
    - helloWorldApp class gets defined, but that code does NOT run yet.
    - we call a method called "application" from the web library that passes in our urls variable and it gives us back something we store into the variable app
    - then we call run() from that app variable
    - now that program is continuously running __on a Cloud 9 server__, waiting for someone to ask it for information
3.  __When you go to the website in a web browser.__
    - since you're going to the root of https://\<your id>\.c9users.io/, that means you want the "/" page
    - the running program get the request for "/" an based on the urls variable, it knows to use the helloWorldApp
    - when you go to a website, that is called a __get__ request, so now the program knows to go to the helloWorldApp and call the __GET__ method you've filled out
    - the GET method returns a string which web library knows to use and turn into HTML for your browser

### Exercises ###
*For all Exercises questions, please type up the answers into a word doc and submit them to the email:  jdirksen@sanmateohigh.org*

1. Break something in your Hello World app that is not a syntax error.  (Like adding a string and an int together.)
    - What happens when you run the webapp?
    - What happens when you try to load the page now?
        - What do you see in the browser?
        - What do you see in the terminal?
 2.  Note that once you start the webapp it keeps running, but you can stop it by pressing the red square stop button.  What happens if you stop your program from running and then try to reload the page?
3.  Update your Hello World app so it prints a message that includes your name.  And then give that link to one of your classmates that are also working on this project and make sure they can load it from their browser and see the correct message.  (Paste the link to this page as the answer to this question.)

### Adding another page (endpoint) ###
1.  Let's say we wanted to add more pages (also called an endpoint).  This is an example of how we can do that.
![two pages](https://github.com/ttwu/2nd-semester-introduction-to-computer-science-principles/blob/master/units/5b_unit/webapp07.PNG?raw=true)

## Exercises ##
4.  What do you think the second link will be?  And what you will see if you go to the second link?  (Type it up the code, run it and confirm.)  Did anything happen that was unexpected?
5.  Add another 4 pages that adapt your answers from lab 4.03.  (You must use for loops to build the results like in your answers from the previous lab.)
    - https://\<your id>\.c9users.io/draw_7     should print
        ![draw_7](https://github.com/ttwu/2nd-semester-introduction-to-computer-science-principles/blob/master/units/5b_unit/webapp08.PNG?raw=true)
    - https://\<your id>\.c9users.io/stars_and_stripes     should print
        ![stars_and_stripes](https://github.com/ttwu/2nd-semester-introduction-to-computer-science-principles/blob/master/units/5b_unit/webapp09.PNG?raw=true)
    - https://\<your id>\.c9users.io/increasing_triangle     should print
        ![increasing_triangle](https://github.com/ttwu/2nd-semester-introduction-to-computer-science-principles/blob/master/units/5b_unit/webapp10.PNG?raw=true)
    - https://\<your id>\.c9users.io/vertical_stars_and_stripes     should print
        ![vertical_stars_and_stripes](https://github.com/ttwu/2nd-semester-introduction-to-computer-science-principles/blob/master/units/5b_unit/webapp11.PNG?raw=true)
    (Paste links to all 4 as the answer to this question.)
    
### Let's make it more interesting ###
6.  __Let's add inputs.__  
    - here's an example of how you add an input that you can access in your GET method
    ![input](https://github.com/ttwu/2nd-semester-introduction-to-computer-science-principles/blob/master/units/5b_unit/webapp12.PNG?raw=true)

### Exercise ###
6.  Type up the previous example and run it.  
    - What do you get when you go to it https://\<your id>\.c9users.io/repeatWord
    - What about if you add an argument to it like this?  https://\<your id>\.c9users.io/repeatWord?repeatThis=hihi
    - What about if you add two arguments to it like this?  https://\<your id>\.c9users.io/repeatWord?repeatThis=hihi&numberOfTimes=2
    - What is the link to use if you want the page to print "beep" 5 times?
7.  Can you describe the pattern of the link?
    - what comes before the ? in the link?
    - what comes after the ? in the link?
    - what does = do?
    - what does & do?
    - (If any of this is confusing, chat with your classmates who are also working on this unit.)
8.  Write another endpoint such that
    - https://\<your id>\.c9users.io/removeLetters?removeLetter=a&fromWord=blahblah
    - prints out a result of "blhblh"
9.  Write another endpoint such that is a short madlib story that takes in 5 words.  It can look something like this example:
    - https://\<your id>\.c9users.io/madlib?noun1=chicken&noun2=bike&verb1=skip&adjective1=bloated&noun3=squirrel
    - It might print out "Yesterday I went to the San Mateo Department of *chicken* and filled out a form for a *bike* form.  When I was done, I decided to *skip* home but was attacked by a *bloated squirrel*.
    - *Make up your own story, and feel free to use more words.*
    - For your answer to this question, paste a link with sample input words.  Your page should still work if I decide to change up the arguments in your link

### What kind of input can we not do with python in a web app?  ###
- The kind of interaction we had with a regular python app where we can enter input and the program responds and prints something else out, we cannot do with python on a webapp.  Like with the text-based adventure game, or Oregon Trail where the program asks for a command, we type something in, and then the program prints something new and asks us for more input (repeated indefinitely), this we cannot do in python on this webapp.
- __Why not?__ Since python is acting only on the backend, its job is to send us HTML and javascript code we will need to render the page.  We send it data when we request a page, and it sends us that page.  The interaction that we want when in a web page should be implemented in the javascript layer, because javascript is the language of internet browsers.  We won't go into javascript in this class any further in this class, but there are many excellent resources on the web that can get you started.  (Let me know if you want somewhere to start.)

### Let's do some HTML ###
- HTML is not technically a programming language.  It is a markup language but it's important because it lets us define what elements go on a webpage, and how they should be arranged and how they should appear.  Basically it lets us make this page pretty.
- Here is an example of a webapp that writes some HTML.
- ![html](https://github.com/ttwu/2nd-semester-introduction-to-computer-science-principles/blob/master/units/5b_unit/webapp13.PNG?raw=true)

### Exercises ###
10.  Type up the example above and run it and go to the page and see what you get.

### Easier way to do html with a python app - Templating! ###
- But as you can imagine it gets pretty cluttered and confusing since it all has to be inside a string.  An easier way to write HTML that you will use for an app is by using templating.
- To start, create a folder in your webapps directory called "templates".
- Inside that folder create a file called templatedPageApp.html and type up this inside.
- ![html](https://github.com/ttwu/2nd-semester-introduction-to-computer-science-principles/blob/master/units/5b_unit/webapp14.PNG?raw=true)
- Next, create a new python file and type this up in it
- ![html](https://github.com/ttwu/2nd-semester-introduction-to-computer-science-principles/blob/master/units/5b_unit/webapp15.PNG?raw=true)
- Note:
    - line 12 is the line that says look in the templates folder for html files
    - line 13 uses the render object created from web.template.render to grab the templatedPageApp.html file and render the contents of that.

### Exercises ###
11.  What do you see when you go to that page?  How would you change that page so that it shows different image?
12.  Spend some time learning some more HTML tags and adding more elements onto the html page.  Look through the following resources.  (Some suggestions to look up and try if you're feeling overwhelmed.  How do you add an image?  How do you change the background color?  How do you change the font color?  How do you change fonts?  How do you add a link to somewhere?  How do you add a button?)
    - http://www.w3schools.com/html/
    - http://htmldog.com/guides/html/beginner/
    - https://www.codecademy.com/learn/web

### So why do we want to do this? ###
At the end of all this work, it might have seem that we have taken some steps forwards and some steps back.  

Let's look at the pluses and minuses.

    + We can turn a python app into a web app and we can access it from the internet.
    - We can't do inputs as easily as a regular python app, so some of our apps would need to be reimplemented in javascript to work on the web.
    + We can utilize HTML and javascript to enrich our app with colors and images, etc.
    - HTML and javascript what we need to make the frontend more interesting.  So why do we need python?
    
That final question is an important one.  The answer is that we barely scratched the surface of what python can do on the web server.  In our examples we only used python to build some strings, but you can use python to access databases (pull your stored images from twitter or tumblr), to maintain your own database (upload and store musical clips), to query other services (ask weather.com for the latest weather information), etc.

You should think of python in the webapp use case as the language that will do the behind the scenes work of gathering information, then it packages that data with HTML and javascript.  HTML and javascript do the front-facing work of configuring how the webpage will look to you.
