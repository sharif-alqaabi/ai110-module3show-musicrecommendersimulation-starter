"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import DEFAULT_WEIGHTS, load_songs, recommend_songs, recommend_songs_with_config

PROFILE_LIBRARY = {
    "High-Energy Pop": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "danceability": 0.8,
        "likes_acoustic": False,
        "tempo_bpm": 122,
        "valence": 0.82,
    },
    "Chill Lofi": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.35,
        "danceability": 0.55,
        "likes_acoustic": True,
        "tempo_bpm": 76,
        "valence": 0.60,
    },
    "Deep Intense Rock": {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.92,
        "danceability": 0.50,
        "likes_acoustic": False,
        "tempo_bpm": 150,
        "valence": 0.45,
    },
    "Conflicted Edge Case": {
        "genre": "classical",
        "mood": "moody",
        "energy": 0.92,
        "danceability": 0.25,
        "likes_acoustic": True,
        "tempo_bpm": 65,
        "valence": 0.30,
    },
}

EXPERIMENTAL_WEIGHTS = {
    **DEFAULT_WEIGHTS,
    "genre": 1.0,
    "energy": 3.0,
}


def print_recommendations(title: str, recommendations: list[tuple[dict, float, str]]) -> None:
    """Print a readable block of recommendations for one profile."""
    print(f"\n=== {title} ===\n")
    for index, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        print(f"{index}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f}")
        print(f"   Reasons: {explanation}")
        print(f"   Vibe: {song['genre']}, {song['mood']}, energy {song['energy']:.2f}")
        print()


def run_profile(name: str, user_prefs: dict, songs: list[dict]) -> None:
    """Run and print one recommendation profile using the default logic."""
    recommendations = recommend_songs(user_prefs, songs, k=5)
    print_recommendations(name, recommendations)


def run_experiment(profile_name: str, user_prefs: dict, songs: list[dict]) -> None:
    """Compare baseline recommendations with an energy-heavy experiment."""
    baseline = recommend_songs(user_prefs, songs, k=5)
    experiment = recommend_songs_with_config(
        user_prefs,
        songs,
        k=5,
        weights=EXPERIMENTAL_WEIGHTS,
    )

    print("\n=== Weight Shift Experiment ===")
    print("Baseline weights: genre 2.0, mood 1.5, energy 1.5")
    print("Experimental weights: genre 1.0, mood 1.5, energy 3.0")
    print(f"Profile tested: {profile_name}")

    print_recommendations("Baseline Top 5", baseline)
    print_recommendations("Experimental Top 5", experiment)


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    for name, user_prefs in PROFILE_LIBRARY.items():
        run_profile(name, user_prefs, songs)

    run_experiment("High-Energy Pop", PROFILE_LIBRARY["High-Energy Pop"], songs)


if __name__ == "__main__":
    main()
