from jikanpy import Jikan

jikan = Jikan()

# search by fetching id instead of hardcoding
search_result = jikan.search("manga", "One Piece")
one_piece_id = search_result["data"][0]["mal_id"]
one_piece = jikan.manga(one_piece_id)

# api json format follows a data dictionary with a nested dictionary with all relevant fields
# print(one_piece["data"].keys())

member_count = one_piece["data"]["members"]
score_count = one_piece["data"]["score"]
print(member_count)
print(score_count)
