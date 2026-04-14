import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top-k songs ranked by fit with the user profile."""
        scored_songs = sorted(
            self.songs,
            key=lambda song: self._score_song_object(user, song),
            reverse=True,
        )
        return scored_songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Describe why a song matched the user profile."""
        _, reasons = self._score_song_object(user, song, return_reasons=True)
        return ", ".join(reasons)

    def _score_song_object(
        self,
        user: UserProfile,
        song: Song,
        return_reasons: bool = False,
    ) -> float | Tuple[float, List[str]]:
        """Score a Song dataclass using the same logic as the functional API."""
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        song_dict = {
            "genre": song.genre,
            "mood": song.mood,
            "energy": song.energy,
            "tempo_bpm": song.tempo_bpm,
            "valence": song.valence,
            "danceability": song.danceability,
            "acousticness": song.acousticness,
        }
        score, reasons = score_song(user_prefs, song_dict)
        if return_reasons:
            return score, reasons
        return score

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from CSV and convert numeric fields into math-friendly types."""
    songs: List[Dict] = []
    int_fields = {"id"}
    float_fields = {"energy", "tempo_bpm", "valence", "danceability", "acousticness"}

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            song: Dict = {}
            for key, value in row.items():
                if key in int_fields:
                    song[key] = int(value)
                elif key in float_fields:
                    song[key] = float(value)
                else:
                    song[key] = value
            songs.append(song)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against user preferences and explain the main contributors."""
    score = 0.0
    reasons: List[str] = []

    if song["genre"] == user_prefs.get("genre"):
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"] == user_prefs.get("mood"):
        score += 1.5
        reasons.append("mood match (+1.5)")

    target_energy = user_prefs.get("energy")
    if target_energy is not None:
        energy_similarity = max(0.0, 1 - abs(song["energy"] - target_energy))
        energy_points = round(energy_similarity * 1.5, 2)
        score += energy_points
        reasons.append(f"energy similarity (+{energy_points:.2f})")

    target_danceability = user_prefs.get("danceability", target_energy)
    if target_danceability is not None:
        dance_similarity = max(0.0, 1 - abs(song["danceability"] - target_danceability))
        dance_points = round(dance_similarity * 0.75, 2)
        score += dance_points
        reasons.append(f"danceability similarity (+{dance_points:.2f})")

    likes_acoustic = user_prefs.get("likes_acoustic")
    if likes_acoustic is not None:
        acoustic_match = song["acousticness"] if likes_acoustic else 1 - song["acousticness"]
        acoustic_points = round(acoustic_match * 0.5, 2)
        score += acoustic_points
        reasons.append(f"acoustic fit (+{acoustic_points:.2f})")

    target_tempo = user_prefs.get("tempo_bpm")
    if target_tempo is not None:
        tempo_similarity = max(0.0, 1 - (abs(song["tempo_bpm"] - target_tempo) / 100))
        tempo_points = round(tempo_similarity * 0.25, 2)
        score += tempo_points
        reasons.append(f"tempo similarity (+{tempo_points:.2f})")

    target_valence = user_prefs.get("valence")
    if target_valence is not None:
        valence_similarity = max(0.0, 1 - abs(song["valence"] - target_valence))
        valence_points = round(valence_similarity * 0.25, 2)
        score += valence_points
        reasons.append(f"valence similarity (+{valence_points:.2f})")

    return round(score, 2), reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score, rank, and return the top-k songs with short explanations."""
    scored_songs: List[Tuple[Dict, float, str]] = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_songs.append((song, score, explanation))

    ranked_songs = sorted(scored_songs, key=lambda item: item[1], reverse=True)
    return ranked_songs[:k]
