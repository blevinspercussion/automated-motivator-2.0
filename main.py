from ai_processing import ai_processing
from image_processing import image_processing
from facebook_upload import facebook_upload


def main():
    # image_prompt = ai_processing.construct_image_prompt
    # quote_prompt = ai_processing.construct_text_prompt

    ai_processing.generate_image(ai_processing.construct_image_prompt())
    quote = ai_processing.generate_quote(ai_processing.construct_text_prompt())

    image_processing.text_overlay(quote)

    facebook_upload(quote)


if __name__ == "__main__":
    main()
