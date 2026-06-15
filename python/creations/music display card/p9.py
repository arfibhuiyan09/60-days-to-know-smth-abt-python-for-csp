def display_card(song_name, artist_name, plays, score, genre_tag):
      print(f"Title:  {song_name}")
      print(f"Artist:  {artist_name}") 
      print(f"Views:   {plays}")
      print(f"Rating:  {score}/100")
      print(f"Tag:  {genre_tag}")

choice = input("do you want to generate a stat card for a song? (Y/N)   ").lower()
def calculate_rating(plays,
                      likes,
                        comments):
    calculation = (likes * 0.5 + comments * 0.3 + plays * 0.2) / 10000
    return calculation

def get_genre_tag(score):
    if score >= 90:
        tag = "Chart Topper"
    elif score >= 70:
        tag = "Fan Favourite"
    elif score >= 50:
        tag = "Kinda Underrated"
    elif score >= 25:
        tag = "Niche, W taste"
    else:
        tag = "Hidden Gem"
    
    return tag
if choice == "y":
    song_name = input("ok first, what is the song you want a stat card for?   ")
    artist_name = input(f"who is the artist for {song_name}?    ")
    plays = float(input(f"enter the view count for {song_name}: (numerically)   "))
    likes = float(input(f"enter the like count for {song_name}: (numerically)   "))
    comments = float(input(f"enter the comment count for {song_name}: (numerically)   "))
    score = calculate_rating(plays,likes,comments)
    print(f"your score is {score}!")
    genre_tag = get_genre_tag(score)
    print("\n")
    print("here is your stats card:")
    display_card(song_name, artist_name, plays, score, genre_tag)
elif choice == "n":
    print("oka")
else:
    print(f"--> Error: '{choice}' is an invalid prompt answer!")
