import facebook

FACEBOOK_API_TOKEN = "EAAMIlaVy5J4BO6O27848SolV87KZAtelWaa8881e545L8zgzfJdNPJxDVWzb3YZBmYZAeBKL8QaSbOa9ZCmWTYYXmYsdnZC7lQZBDvVbdZCZA7YXCOgmi1gZBCTpjHWrSXNwgboOp1oyjeTxgPE28KUI8JqwARmjO9ztq2vZCa6JyEbsvvhfiA3ZBMz4PV7lU5bZA8S1NBbbWjQ6kWQ0TCBURQya"
FACEBOOK_PAGE_ID = "109154062093016"


def facebook_upload(quote, api_token=FACEBOOK_API_TOKEN, page_id=FACEBOOK_PAGE_ID):

    graph = facebook.GraphAPI(FACEBOOK_API_TOKEN)

    graph.put_photo(
        image=open("final.png", "rb"),
        message=f"{quote} #DailyMotivation #DailyAffirmation #motivation #quotes #QuotesToLiveBy",
    )


if __name__ == "__main__":
    facebook_upload(
        "In the depths of solitude, the heart unfolds, whispering truths untouched by the clamor of the world. Loneliness, a sacred pause where introspection reigns, unveils the essence of our being, illuminating the path to self-discovery."
    )
