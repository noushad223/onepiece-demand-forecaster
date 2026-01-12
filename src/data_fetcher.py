from jikanpy import Jikan
import time
import pandas as pd
import datetime
import os

jikan = Jikan()
SLEEP = 0.5
CURRENT_DATE = datetime.date.today()
BASE_DIR = os.path.dirname(__file__)
FILE_NAME = os.path.join(BASE_DIR, "onepiece_tracker.csv")

# search by fetching id instead of hardcoding

# manga
search_result_manga = jikan.search("manga", "One Piece")
time.sleep(SLEEP)
one_piece_manga_id = search_result_manga["data"][0]["mal_id"]
one_piece_manga = jikan.manga(one_piece_manga_id)
time.sleep(SLEEP)

# anime
search_result_anime = jikan.search("anime", "One Piece")
time.sleep(SLEEP)
one_piece_anime_id = search_result_anime["data"][0]["mal_id"]
one_piece_anime = jikan.anime(one_piece_anime_id)
time.sleep(SLEEP)

# api json format follows a data dictionary with a nested dictionary with all relevant fields
# print(one_piece_manga["data"].keys())
# print(one_piece_anime["data"].keys())

member_count = one_piece_manga["data"]["members"] + one_piece_anime["data"]["members"]
score_count = round(
    (one_piece_manga["data"]["score"] + one_piece_anime["data"]["score"]) / 2, 1
)  # find average score
popularity_manga = one_piece_manga["data"]["popularity"]
popularity_anime = one_piece_anime["data"]["popularity"]

current_entry = {
    "date": CURRENT_DATE.strftime("%Y-%m-%d"),
    "members": member_count,
    "score": score_count,
    "manga_popularity": popularity_manga,
    "anime_popularity": popularity_anime,
}

df = pd.DataFrame([current_entry])
try:
    if not os.path.isfile(FILE_NAME):
        df.to_csv(FILE_NAME, index=False)
    else:
        df_existing = pd.read_csv(FILE_NAME)
        if current_entry["date"] not in df_existing["date"].values:
            df.to_csv(FILE_NAME, mode="a", header=False, index=False)
except (OSError, pd.errors.ParserError) as e:
    print(f"File error: {e}")
