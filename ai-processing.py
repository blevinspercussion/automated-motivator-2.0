from openai import OpenAI
import random
from base64 import b64decode

client = OpenAI(api_key="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")


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

    TIME_OF_DAY = ["morning", "day", "afternoon", "night", "evening", "dawn", "dusk"]

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

    return (
        f"make a {random.choice(QUOTE_TYPE)} quote about {random.choice(QUOTE_TOPICS)}"
    )


def generate_image(image_prompt):
    """
    Takes a prompt as an argument and uses it to generate an ai image using OpenAI Dall-E 3.
    Returns the image data as Base64 JSON.
    """

    response = client.images.generate(
        model="dall-e-3",
        prompt=image_prompt,
        size="1024x1024",
        quality="standard",
        response_format="b64_json",
        n=1,  # number of images generated (dall-e-3 only supports 1)
    )

    return response


def generate_quote(quote_prompt):
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


def main():
    print(construct_image_prompt(), "\n", construct_text_prompt())
    generate_image(construct_image_prompt())
    generate_quote(construct_text_prompt())


if __name__ == "__main__":
    main()
