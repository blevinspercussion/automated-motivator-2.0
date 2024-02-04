from openai import OpenAI
import random
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key=API_KEY)


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

        image_prompt = f"{random.choice(PICTURE_TYPES)} on a {random.choice(WEATHER_TYPES)} {random.choice(TIME_OF_DAY)} in a {random.choice(STYLE_TYPES)} style"
        print(f"Image prompt: {image_prompt}")

        return image_prompt

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

        prompt = f"make a short {random.choice(QUOTE_TYPE)} quote about {random.choice(QUOTE_TOPICS)}"
        print(f"Text prompt: {prompt}")

        return prompt

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
            n=1,  # number of images generated (dall-e-3 only supports 1)
        )

        image_url = response.data[0].url

        img_data = requests.get(image_url).content
        with open("image.png", "wb") as handler:
            handler.write(img_data)

        print("Image generated.")

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

        print(f"Quote: {quote}")
        return quote


def main():

    ai_processing.generate_image(ai_processing.construct_image_prompt())
    ai_processing.generate_quote(ai_processing.construct_text_prompt())


if __name__ == "__main__":
    main()
