# The Automated Motivator 

## Description
The automated motivator is a simple Python program that automates posting to a Facebook page while leveraging the power of OpenAI's Chat GPT and Dall-E APIs.
It uses the OpenAI APIs to generate a pseudorandom impage creation prompt and a motivational quote. It then uses the PIL library to superimpose the quote onto 
the image and create a watermark for the Facebook page. Finally, it uploads the resulting image to the Facebook page and adds a text post comprised of the 
generate quate and several hashtags.

## Background

I came up with the idea for this project while off work for a couple of weeks. I wanted to learn how to use Open AI's APIs and I was also interested in 
automating the uploading of Facebook content. I was scrolling through Facebook when I began to see a lot of posts that included banal motivational quotes 
superimposed over a calm background, and I began to wonder if I could automate this type of content at the click of a button. And so the idea was born.

## Project Structure

The project consists of four Python scripts: ai_processing.py, image_processing.py, facebook_upload.py, and main.py.

### Setup

In order to use this project, begin by cloning the repo locally. You will need a font file. I have included Roboto-Black.ttf, but you should be able to use any font, though you may have to adjust the font size (read the section on image_processing.py below). You will also need a .env file with your environment variables including your OpenAI API key and your Facebook page access token.

### ai_processing.py

This file is responsible for generating the text and using it to create the image and quote text using the OpenAI API. It includes one class, ai_processing, with four methods (not counting the __init__ method).

At the top of the script, after the imports, it loads the environment variables with load_dotenv(). Link the API_KEY variable to your corresponding variable in your .env file, then create the client using your API key.

1. **construct_image_prompt** is responsible for generating a prompt that will be used to generate the image. You can feel free to edit the list variables as you see fit.

2. **generate_text_prompt** creates the prompt that will be used to generate the quote. As with the previous method, you can edit the list variables however you like to get your desired result.

3. **generate_image** takes the image prompt and the client as an argument and uses them to generate an image using OpenAI's Dall-E 3 model. The image is saved into the current working directory as "image.png".

4. **generate_quote" takes the quote prompt and the client as an argument as uses the quote prompt to generate a quote using OpenAI's GPT 3.5 Turbo model.

The **main.py** function runs the entire process.

### image_processing.py

This file is responsible for handling all of the image manipulation. It consists of one class, image_processing, with one method.

1. **text_overlay** takes the previously generated quote as an argument. I begins by setting the font size, font file, and text (the quote argument) and sets the text to wrap at 25 characters. The font variables (size, textwrap) may have to be altered if you use a different font. It then opens the image.png file, sets the position of the text, and draws it to the image. The rest of method creates and draws the watermark and saves it to the current working directory as final.png. You can alter this part to add your own watermark.

The execution block runs the code with a placeholder quote for testing purposes.

### facebook_upload.py 

This file is simple as it just uploads the final image to Facebook. Bu sure to correctly link the FACEBOOK_API_TOKEN variable to the corresponding variable in your .env file. The main execution block uploads the file with placeholder text for testing purposes.

### main.py

This file imports the necessary functions and classes from the other files and sets everything into motion. If your environment variables are correct, everything should work by running this file from your code editor/IDE or from the command line.

### How to use

Clone the repo locally. Create the .env file with your environment variables (OPENAI_API_KEY and FACEBOOK_PAGE_ID), install dependencies (pip install -r requirements.txt), and run the main file.(**python main.py** on Windows or **python3 main.py** on Linux/Mac).
