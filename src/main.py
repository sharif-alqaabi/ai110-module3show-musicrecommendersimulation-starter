"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "danceability": 0.8,
        "likes_acoustic": False,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print(f"Loaded songs: {len(songs)}")
    print("\nTop recommendations:\n")
    for rec in recommendations:
        song, score, explanation = rec
        print(f"{song['title']} by {song['artist']}")
        print(f"  Score: {score:.2f}")
        print(f"  Reasons: {explanation}")
        print(f"  Vibe: {song['genre']}, {song['mood']}, energy {song['energy']:.2f}")
        print()


if __name__ == "__main__":
    main()
