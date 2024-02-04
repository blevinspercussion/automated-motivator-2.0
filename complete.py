from openai import OpenAI
import random
import requests
import aiohttp
import asyncio

from pathlib import Path
import textwrap
from PIL import Image, ImageFont, ImageDraw

import facebook

client = OpenAI(api_key="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")

FACEBOOK_API_TOKEN = "EAAMIlaVy5J4BO9eXjp2H9c519fVooiAP6szXpm6AY51FJRsNhwClj68ZAygkewi0g80lmXyCk54ZAKoJVNaBN9rzgqlOGN0939aIuFhEc1hBme7VyoTrZCsYX0YkZCrpLQyf4bBbWyKlzAZB3zSg3tDd4zInwkXsZBPICgDZCSurhPD008SzL5TPZCaQIzdDfi26AUF4RK26biJTYOS9GY6f"
FACEBOOK_PAGE_ID = "109154062093016"


class ai_processing:
    def __init__(self, client):
        self.client = client

    def construct_image_prompt():
        """
        Constructs a pseudo-random image prompt for an ai model, and returns the prompt as a string.
        """

        PICTURE_TYPES = [
            "sky",
            "nature",
            "woods",
            "outer space",
            "ocean",
            "flowers",
            "gradient color",
            "liminal space",
            "lake",
            "pond",
            "forest",
            "water",
            "trees",
            "desert",
        ]

        WEATHER_TYPES = [
            "clear",
            "cloudy",
            "rainy",
            "overcast",
            "stormy",
            "sunny",
            "bright",
            "gloomy",
        ]

        STYLE_TYPES = [
            "anime",
            "photographic",
            "painted",
            "hand drawn",
            "hand painted",
            "pixel art",
            "oil painting",
            "science fiction",
            "fantasy",
            "synthwave",
            "cyberpunk",
            "digital art",
            "crayon",
            "single line drawing",
            "3d rendered",
        ]

        TIME_OF_DAY = [
            "morning",
            "day",
            "afternoon",
            "night",
            "evening",
            "dawn",
            "dusk",
        ]

        return f"{random.choice(PICTURE_TYPES)} on a {random.choice(WEATHER_TYPES)} {random.choice(TIME_OF_DAY)} in a {random.choice(STYLE_TYPES)} style"

    def construct_text_prompt():
        """
        Constructs a pseudo-random prompt for an ai to generate a quote and returns the prompt as a string.
        """

        QUOTE_TYPE = [
            "inspirational",
            "motivational",
            "sympathetic",
            "heartfelt",
            "happy",
            "friendly",
            "introspective",
            "reflective",
            "nostalgic",
        ]

        QUOTE_TOPICS = [
            "love",
            "determination",
            "hard work",
            "perserverence",
            "gratitude",
            "friendship",
            "happiness",
            "success",
            "generosity",
            "loss",
            "adversity",
            "music",
            "family",
            "loneliness",
            "home",
            "simple living",
            "time",
            "life",
            "mental health",
            "the future",
            "lost love",
            "new beginnings",
            "humility",
        ]

        return f"make a short {random.choice(QUOTE_TYPE)} quote about {random.choice(QUOTE_TOPICS)}"

    def generate_image(image_prompt, client=client):
        """
        Takes a prompt as an argument and uses it to generate an ai image using OpenAI Dall-E 3.
        Returns the image URL.
        """

        print("Generating image...")
        response = client.images.generate(
            model="dall-e-3",
            prompt=image_prompt,
            size="1024x1024",
            quality="standard",
            response_format="url",
            n=1,  # number of images generated (dall-e-3 only supports 1)
        )

        image_url = response.data[0].url

        img_data = requests.get(image_url).content
        with open("test.png", "wb") as handler:
            handler.write(img_data)

    def generate_quote(quote_prompt, client=client):
        """
        Takes a prompt as an argument and uses it to create a quote using OpenAI GPT 3.5 Turbo
        """

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a brilliant poet and orator that loves dispensing wisdom.",
                },
                {"role": "user", "content": quote_prompt},
            ],
        )

        quote = response.choices[0].message.content

        print(quote)
        return quote


class image_processing:
    def text_overlay(quote):
        print("writing text overlay...")
        IMAGE_FILE = Path.cwd() / "test.png"
        font_size = 72
        text_font = ImageFont.truetype("Roboto-Black.ttf", size=font_size)
        text = quote
        text = textwrap.fill(text=text, width=25)

        try:
            image = Image.open(IMAGE_FILE)
        except Exception as e:
            print(f"Error opening image file: {e}")
            return

        image_editable = ImageDraw.Draw(image)
        position = (130, 50)

        image_editable.text(
            position,
            text,
            (255, 255, 255),
            font=text_font,
            stroke_width=3,
            stroke_fill=(0, 0, 0),
        )

        # Watermark
        width, height = image.size

        draw = ImageDraw.Draw(image)
        watermark_text = "facebook.com/WordsToMotivate"
        watermark_font_size = 50
        watermark_font = ImageFont.truetype(
            "Roboto-Black.ttf", size=watermark_font_size
        )

        wm_width, wm_height = draw.textsize(watermark_text, watermark_font)

        # Calculate x, y coordinates of the text
        margin = 10
        x = width - wm_width - margin
        y = height - wm_height - margin

        # Draw watermark
        draw.text((x, y), watermark_text, font=watermark_font)

        image.save(Path.cwd() / "final.png")


def facebook_upload(quote, api_token=FACEBOOK_API_TOKEN, page_id=FACEBOOK_PAGE_ID):

    graph = facebook.GraphAPI(FACEBOOK_API_TOKEN)

    graph.put_photo(
        image=open("final.png", "rb"),
        message=f"{quote} #DailyMotivation #DailyAffirmation #motivation #quotes #QuotesToLiveBy",
    )


def main():
    image_prompt = ai_processing.construct_image_prompt
    quote_prompt = ai_processing.construct_text_prompt

    ai_processing.generate_image(image_prompt)
    quote = ai_processing.generate_quote(quote_prompt)

    image_processing.text_overlay(quote)

    facebook_upload(quote)


if __name__ == "__main__":
    main()
