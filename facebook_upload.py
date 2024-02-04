import facebook
import os
from dotenv import load_dotenv


def facebook_upload(quote):
    FACEBOOK_API_TOKEN = os.environ.get("FACEBOOK_API_TOKEN")
    FACEBOOK_PAGE_ID = os.environ.get("FACEBOOK_PAGE_ID")

    graph = facebook.GraphAPI(FACEBOOK_API_TOKEN)

    print("Uploading to Facebook...")

    graph.put_photo(
        image=open("final.png", "rb"),
        message=f"{quote} #DailyMotivation #DailyAffirmation #motivation #quotes #QuotesToLiveBy",
    )

    print("Upload complete!")


if __name__ == "__main__":
    facebook_upload(
        "In the depths of solitude, the heart unfolds, whispering truths untouched by the clamor of the world. Loneliness, a sacred pause where introspection reigns, unveils the essence of our being, illuminating the path to self-discovery."
    )
