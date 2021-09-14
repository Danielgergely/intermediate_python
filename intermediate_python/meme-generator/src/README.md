A Meme generator application
-

This Project is the second project from the Python intermediate course from udacity.

This application reads multiple images in .png or .jpeg formats using the pillow library. The images are resized to
a width of 500px. At the same time quotes are read in by the system from multiple file types (PDF, CSV, Text and Word).
These quotes are passed on to the meme generator, which puts these on the images. These images are then saved to 
a specified location. 

Setup:


Project structure
 - app.py runs the whole application. It is responsible for the setup of the whole application and the launching of the
webapp
 - meme.py receives the quotes and the images and forwards it to the meme_creator, which then creates the image with a
caption
 - in the meme_generator package we find the meme_creator file. As mentioned above, this file creates a meme from an
image and a quote
 - in the quote_engine package are all the different ingestors which read different file types and return a quote to
caller.