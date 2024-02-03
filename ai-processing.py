from openai import OpenAI
import random
from base64 import b64decode

client = OpenAI(api_key="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")


def construct_image_prompt():
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
        "pold",
        "forest",
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


def generate_image():
    image_prompt = construct_image_prompt()

    response = client.images.generate(
        model="dall-e-3",
        prompt=image_prompt,
        size="1024x1024",
        quality="standard",
        response_format="b64_json",
        n=1,  # number of images generated (dall-e-3 only supports 1)
    )

    return response


if __name__ == "__main__":
    print(construct_image_prompt(), "\n", construct_text_prompt())
    generate_image()
