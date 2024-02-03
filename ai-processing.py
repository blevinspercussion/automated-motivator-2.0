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


if __name__ == "__main__":
    pass
