from openai import OpenAI
import random


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

    QUOTE_ADJECTIVES = [
        "joy",
        "loss",
        "bitterness",
        "hope",
        "grief",
        "happiness",
        "sadness",
        "pain",
        "solace",
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

    return f"make a {random.choice(QUOTE_TYPE)} quote about the {random.choice(QUOTE_ADJECTIVES)} of {random.choice(QUOTE_TOPICS)}"


if __name__ == "__main__":
    print(construct_image_prompt(), "\n", construct_text_prompt())
