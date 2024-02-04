import facebook

FACEBOOK_API_TOKEN = "EAAMIlaVy5J4BO6ZCNv9xW2cvZAtPZBAXmB1iiNkBG8uSYiihyZBYuom6UCiOUUfyZAyzPNGJo4jZBFJ1tc9WPPy0OydIXfoZCdlC7YMIctbogtgnld8hWKHZB2DqhjOoaMysPY91N4KOIeu1UBCTJ0Q0PZBzByzVYOvobIhs3Vp5KLEqOfVaSP51FJsOUjS2236UZBDkpGFoTAUDPb4cZAlin0D"
FACEBOOK_PAGE_ID = "109154062093016"


def facebook_upload(quote, api_token=FACEBOOK_API_TOKEN, page_id=FACEBOOK_PAGE_ID):

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
