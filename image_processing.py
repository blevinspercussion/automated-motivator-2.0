from pathlib import Path
import textwrap
from PIL import Image, ImageFont, ImageDraw, ImageFilter


class image_processing:
    def text_overlay(quote):
        print("Writing text overlay...")
        IMAGE_FILE = Path.cwd() / "image.png"
        font_size = 72
        text_font = ImageFont.truetype("Roboto-Black.ttf", size=font_size)
        # text = quote
        text = textwrap.fill(text=quote, width=25)

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

        # Calculate wm_width and wm_height
        wm_bbox = draw.textbbox((0, 0), watermark_text, font=watermark_font)
        wm_width = wm_bbox[2] - wm_bbox[0]
        wm_height = wm_bbox[3] - wm_bbox[1]

        # Calculate x, y coordinates of the text
        margin = 10
        x = width - wm_width - margin
        y = height - wm_height - margin

        # Draw watermark
        draw.text((x, y), watermark_text, font=watermark_font)

        image.save(Path.cwd() / "final.png")

        print("Image overlay created.")


if __name__ == "__main__":
    image_processing.text_overlay(
        "In the depths of solitude, the heart unfolds, whispering truths untouched by the clamor of the world. Loneliness, a sacred pause where introspection reigns, unveils the essence of our being, illuminating the path to self-discovery."
    )
