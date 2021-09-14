A Meme generator application
-

This Project is the second project from the Python intermediate course from udacity.

This application reads multiple images in .png or .jpeg formats using the pillow library. The images are resized to
a width of 500px. At the same time quotes are read in by the system from multiple file types (PDF, CSV, Text and Word).
These quotes are passed on to the meme generator, which puts these on the images. These images are then saved to 
a specified location. 

Setup:


Project structure
 - app.py runs the whole application in a web-browser. With a click of a button a random meme can be created. There
is also a possibility to create a custom meme by specifying an image url, and a quote along with an author.
 - meme.py runs the whole application in the command line. Specifying aruments "--body", "--author" and "--path" create
a new meme. If nothing is specified, a random image and quote will be chosen from the _data package and saved.
 - in the meme_generator package we find the meme_creator file. This file creates a meme from an image and a quote.
 - in the quote_engine package are all the different ingestors which read different file types and return a quote to
caller.