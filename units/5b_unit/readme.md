# Bonus Unit: Serving Up Python Web Apps #

The general idea is that we can use a python library called [web.py](http://webpy.org/) to serve up web page data.  Cloud 9 stores our programs in the cloud and when we run a program that uses the [web.py](http://webpy.org/) library, it will serve webpages at an address we can access at a location like:
https://<your id>.c9users.io/

### Important notes: ###
1.  __You will need to use python 2__ to use web.py (we have been using python 3 for the rest of the semester).  Make sure to change it before trying to run a program in this unit.
(To change it, go to settings for your workspace
![settings](https://github.com/ttwu/2nd-semester-introduction-to-computer-science-principles/blob/master/units/5b_unit/webapp01.PNG)
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
	![hello world](https://github.com/ttwu/2nd-semester-introduction-to-computer-science-principles/blob/master/units/5b_unit/webapp02.PNG)
	- __Here's how you get it to serve up as a webpage.__
		- Run this in cloud9.  ![run](https://github.com/ttwu/2nd-semester-introduction-to-computer-science-principles/blob/master/units/5b_unit/webapp03.PNG)
		- Look at the terminal and it will tell you the app is running at a url like:  https://<your_cloud9_account_name>.c9users.io
	    ![link](https://github.com/ttwu/2nd-semester-introduction-to-computer-science-principles/blob/master/units/5b_unit/webapp04.PNG)
		- Now you can paste this url into a browser of your choice (chrome, firefox, etc) and you should see
		![link](https://github.com/ttwu/2nd-semester-introduction-to-computer-science-principles/blob/master/units/5b_unit/webapp05.PNG)
    - Also note that after you loaded the page, in your cloud9 terminal, it will show:
    ![log](https://github.com/ttwu/2nd-semester-introduction-to-computer-science-principles/blob/master/units/5b_unit/webapp06.png)
    That shows that our server code got a reqest for the "/" page and it successfully responded.
2.  __The major parts of the webapp__ (Notes are already in comments of provided code.)
    * 1.  need to import web.py (since we need to use this library)
    * 2.  need to create a mapping from url to python classes that will handle the request.
        * *('/', 'helloWorldApp')* means that if someone accesses the root page '/', my helloWorldApp class is the class that will know what information to send back.
    * 3. create a class by the same name as the mapping above.  (in this case, helloWorldApp)
    * 4. inside this class, write a __GET__ method that returns a string.
    * 5. need this chunk of code so that it will run the rest of the code you just wrote.

### Exercises ###
*For these questions, please type up the answers and submit them via Google Classroom.*

1. Break something in your Hello World app that is not a syntax error.  Like adding a string and an int together.
    - What happens when you run the webapp?
    - What happens when you try to load the page now?
        - What do you see in the browser?
        - What do you see in the terminal?
 2.  Note that once you start the webapp it keeps running, but you can stop it by pressing the red square stop button.  What happens if you stop your program from running and then try to reload the page?
3.  Update your Hello World app so it prints a message that includes your name.  And then give that link to one of your classmates that are also working on this project and make sure they can load it from their browser and see the correct message.  (Paste the link to this page as the answer to this question.)

### Adding another page (endpoint) ###
1.  Let's say we wanted to add more pages (also called an endpoint).  This is an example of how we can do that.
![two pages](https://github.com/ttwu/2nd-semester-introduction-to-computer-science-principles/blob/master/units/5b_unit/webapp07.png)

## Exercises ##
4.  What do you think the second link will be?  And what you will see if you go to the second link?  (Type it up and confirm.)
5.  Add another 4 pages that adapt your answers from lab 4.03.  (You must use for loops to build the results like in your answers from the previous lab.)
    - https://<your id>.c9users.io/draw_7     should print
        ![draw_7](https://github.com/ttwu/2nd-semester-introduction-to-computer-science-principles/blob/master/units/5b_unit/webapp08.png)
    - https://<your id>.c9users.io/stars_and_stripes     should print
        ![stars_and_stripes](https://github.com/ttwu/2nd-semester-introduction-to-computer-science-principles/blob/master/units/5b_unit/webapp09.png)
    - https://<your id>.c9users.io/increasing_triangle     should print
        ![increasing_triangle](https://github.com/ttwu/2nd-semester-introduction-to-computer-science-principles/blob/master/units/5b_unit/webapp10.png)
    - https://<your id>.c9users.io/vertical_stars_and_stripes     should print
        ![vertical_stars_and_stripes](https://github.com/ttwu/2nd-semester-introduction-to-computer-science-principles/blob/master/units/5b_unit/webapp11.png)
    (Paste links to all 4 as the answer to this question.)
    
### Let's make it more interesting ###
6.  How do you do inputs?
    - what kind of inputs can we do?
        - we can take an input to build text
            - write a new version of the previous 4 apps so that it takes in a number to know how to build string
        - we can use one page to collect input and send it to another page that uses those answers
            - write an app that asks the user to fill out words for madlibs, then it sends it to another app that uses it to print your mad libs story.
    - what kind of inputs can we NOT do?
        - The kind of interaction we had with a regular python app not on the web, where we can enter input and the program responds and prints something else out, we cannot do with python on a webapp.  Since python is acting only on the backend, its job is to send us HTML and javascript code we will need to render the page.  We send it data when we request a page, and it sends us that page.  The interaction that we want when in a web page should be implemented in the javascript layer, because javascript is the language of internet browsers.  We won't go into javascript in this class any further in this class, but there are many excellent resources on the web that can get you started.  (Let me know if you want somewhere to start.)

7.  __Let's do some HTML__
    - HTML is not technically a programming language.  It is a markup language that lets us place elements onto a webpage.  
    - 

### So why do we want to do this? ###
At the end of all this work, it might have seem that we have taken some steps forwards and some steps back.  

Let's look at the pluses and minuses.

    + We can turn a python app into a web app and we can access it from the internet.
    - We can't do inputs as easily as a regular python app, so some of our apps would need to be reimplemented in javascript to work on the web.
    + We can utilize HTML and javascript to enrich our app with colors and images, etc.
    - HTML and javascript what we need to make the frontend more interesting.  So why do we need python?
    
That final question is an important one.  The answer is that we barely scratched the surface of what python can do on the web server.  In our examples we only used python to build some strings, but you can use python to access databases (pull your stored images from twitter or tumblr), to maintain your own database (upload and store musical clips), to query other services (ask weather.com for the latest weather information), etc.

You should think of python in the webapp use case as the language that will do the behind the scenes work of gathering information, then it packages that data with HTML and javascript.  HTML and javascript do the front-facing work of configuring how the webpage will look to you.
