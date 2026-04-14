# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

My version builds a small, explainable music recommender that scores songs based on how closely they match a user's preferred genre, mood, energy, and overall vibe. Instead of trying to copy a full streaming platform, this project focuses on a simple content-based approach so it is easy to test, understand, and improve.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

My recommender uses a simple content-based filtering approach. That means it recommends songs by comparing the features of each song to the user's personal taste profile, instead of using data from other listeners. In real apps, systems often combine collaborative filtering, which learns from the behavior of similar users, with content-based filtering, which focuses on the attributes of the song itself. My version prioritizes the content-based side because it is easier to understand and explain.

Each `Song` in my system uses features like `genre`, `mood`, `energy`, `tempo_bpm`, `valence`, `danceability`, and `acousticness`. The `UserProfile` stores the listener's `favorite_genre`, `favorite_mood`, `target_energy`, and whether they `like_acoustic` songs. The recommender computes a score for each song by giving the most points to songs that match the user's genre and mood, then adding smaller points when the song's energy and other vibe-related features are close to the user's preferences. After every song gets a score, the system ranks all songs from highest to lowest and recommends the top few songs with the best overall match.

- `Song` features: `genre`, `mood`, `energy`, `tempo_bpm`, `valence`, `danceability`, `acousticness`
- `UserProfile` features: `favorite_genre`, `favorite_mood`, `target_energy`, `likes_acoustic`

Example `UserProfile`:

```python
{
    "favorite_genre": "lofi",
    "favorite_mood": "focused",
    "target_energy": 0.4,
    "likes_acoustic": True
}
```

This profile is broad enough to tell the difference between something like intense rock and chill lofi. A rock song might have high energy, but it would still lose points if its genre and mood do not match the user's study-focused vibe.

Algorithm Recipe:

- Start every song at `0.0` points
- Add `+2.0` points if the song's `genre` matches `favorite_genre`
- Add `+1.5` points if the song's `mood` matches `favorite_mood`
- Add energy similarity points using `1 - abs(song_energy - target_energy)` so songs closer to the user's target earn more points
- Add a small bonus of up to `+0.75` based on how close `danceability` is to the kind of vibe the profile suggests
- Add `+0.5` if `likes_acoustic` is `True` and the song's `acousticness` is high, or if `likes_acoustic` is `False` and the song's `acousticness` is low
- Use `tempo_bpm` and `valence` as small tie-breakers when two songs feel otherwise similar
- Sort songs by total score from highest to lowest
- Return the top `k` songs as the final recommendations

Data Flow:

```mermaid
flowchart LR
    A["User Preferences"] --> B["Load Songs From CSV"]
    B --> C["Loop Through Each Song"]
    C --> D["Score Genre, Mood, Energy, and Other Features"]
    D --> E["Store Song With Total Score"]
    E --> F["Rank All Songs By Score"]
    F --> G["Return Top K Recommendations"]
```

CLI Output Snapshot:

```text
Loaded songs: 18

Top recommendations:

Sunrise City by Neon Echo
  Score: 6.12
  Reasons: genre match (+2.0), mood match (+1.5), energy similarity (+1.47), danceability similarity (+0.74), acoustic fit (+0.41)

Gym Hero by Max Pulse
  Score: 4.46
  Reasons: genre match (+2.0), energy similarity (+1.30), danceability similarity (+0.69), acoustic fit (+0.47)

Rooftop Lights by Indigo Parade
  Score: 4.01
  Reasons: mood match (+1.5), energy similarity (+1.44), danceability similarity (+0.74), acoustic fit (+0.33)
```

Potential bias:

- This system may over-prioritize genre and miss songs from other genres that still match the user's mood
- The small dataset may make the recommender feel narrow because it cannot represent all listener tastes
- A single fixed profile can oversimplify real people, whose music preferences change by time, activity, or context

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

I tested the recommender with four profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and a Conflicted Edge Case profile. The strongest matches were Chill Lofi and Deep Intense Rock because the top songs clearly fit the intended style and mood. I also ran a weight-shift experiment where energy mattered more and genre mattered less. That change moved `Rooftop Lights` above `Gym Hero` for the pop profile, which showed that the ranking is very sensitive to the balance between exact category matches and numerical similarity.

As extra challenges, I extended the project in three ways. First, I added advanced song features like `popularity`, `release_decade`, `detailed_mood_tag`, `instrumentalness`, `liveliness`, and `lyric_density`, then updated the scoring logic to compare those values with math-based similarity rules. Second, I created multiple scoring modes such as `genre-first`, `mood-first`, and `energy-focused` so the user can switch between different ranking strategies. Third, I added a diversity penalty that lowers a song's score if its artist or genre is already overrepresented in the top recommendations, which helps the final list feel more varied and fair.

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

This recommender still has several limits. The catalog is very small, so it cannot represent the full range of music taste and sometimes repeats the same kind of result. It also does not understand lyrics, artist history, culture, or listening context, so it treats taste as a simple set of fixed preferences. The system can also over-prioritize one exact match, especially genre, which can make unusual profiles feel less accurate.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

This project helped me see that recommendations do not need to be very complicated to feel convincing. Even a simple scoring system can produce results that seem smart when the features are chosen well and the weights reflect a clear idea of what a listener wants. I also learned that ranking is just as important as scoring, because even small changes in the weights can move a different song into the top spot.

I also learned how bias can appear in a small system. When one genre or mood gets too much weight, the recommender can ignore songs that match the listener in other important ways. The edge-case profile made that very clear, because the system rewarded an exact classical match even when the energy target did not fit well. That made me think more carefully about how real-world recommenders can create filter bubbles or unfair patterns if their scoring rules are not balanced.
## Screenshots

![alt text](<Screenshot 2026-04-14 at 12.19.00 PM.png>)
![alt text](<Screenshot 2026-04-14 at 12.35.39 PM.png>) 
![alt text](<Screenshot 2026-04-14 at 12.35.28 PM.png>) 
![alt text](<Screenshot 2026-04-14 at 12.35.21 PM.png>) 
![alt text](<Screenshot 2026-04-14 at 12.35.10 PM.png>)
