# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

**VibeMatch 1.0**

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

This recommender suggests songs from a small classroom music catalog based on a user's preferred genre, mood, energy, and acoustic feel. It assumes that a user's taste can be described with a few simple preferences and that songs with similar features will feel like good matches. This project is for classroom exploration, not for real users or real streaming decisions.

Intended use: learning how recommendation systems score and rank items in a simple, transparent way.

Non-intended use: real music product recommendations, high-stakes decisions, or representing a person's full music taste.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

My model looks at each song's genre, mood, energy, danceability, acousticness, tempo, and valence. It also looks at the user's target preferences for those same kinds of features. The system gives the biggest points for matching genre and mood, then gives smaller points when the song's numbers are close to the user's target values. After that, it ranks all songs by total score and recommends the top results. Compared with the starter logic, I added more features, explanation reasons, and a clearer scoring recipe.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The dataset has 18 songs. I started with the 10-song starter file and added 8 more songs to make the catalog more diverse. The features include `genre`, `mood`, `energy`, `tempo_bpm`, `valence`, `danceability`, and `acousticness`. The catalog covers styles like pop, lofi, rock, ambient, jazz, synthwave, EDM, folk, R&B, metal, country, disco, hip hop, and classical. Even with that expansion, the dataset is still very small and misses many important parts of music taste, like lyrics, language, culture, context, and repeated listening habits.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

This system works best when the user's preferences are clear and consistent. It did a good job with profiles like Chill Lofi and Deep Intense Rock because the top recommendations matched the expected vibe very closely. The scoring also captures an important real pattern: songs feel more relevant when categorical features like genre and mood line up with continuous features like energy. I also like that the system is easy to explain because every recommendation comes with reasons.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

One weakness I found is that the system can over-reward a single exact category match, especially for `genre`, even when the rest of the song does not fully match the listener's intent. The "Conflicted Edge Case" profile showed this clearly: `Quiet Constellations` ranked first mostly because it matched `classical`, even though its energy level was far away from the requested 0.92 target. The small dataset also creates a filter-bubble effect because some genres only have one or two examples, so the recommender has very few alternatives to compare. Another limitation is that the model does not understand lyrics, context, or changing moods across the day, so it treats music taste as a fixed set of numbers instead of something flexible. This means the system may feel more accurate for common profiles like pop, lofi, or rock than for unusual or mixed preferences.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I evaluated the recommender with four profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and a Conflicted Edge Case profile that combined `classical`, `moody`, and very high energy. I looked at the top 5 songs for each profile and checked whether the results matched my musical intuition based on genre, mood, energy, and acousticness. The strongest results were for the Chill Lofi and Deep Intense Rock profiles, where the top song clearly matched the intended vibe: `Library Rain` for lofi and `Storm Runner` for rock. What surprised me most was the edge case profile, because the system still ranked a classical song first even though its energy was a poor match, which showed that exact category weights can dominate the final ranking. I also ran a weight-shift experiment where energy importance was doubled and genre importance was cut in half, and that change pushed `Rooftop Lights` above `Gym Hero` for the pop profile, showing that the recommender is sensitive to the balance between category matches and numerical similarity.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

If I kept developing this model, I would add more songs so the recommender had better variety and less risk of narrow results. I would also improve diversity so the top 5 list does not feel too repetitive when one feature dominates. Another improvement would be to support more complex users, such as people who like different music for studying, workouts, and relaxing. I would also like to add better explanations that summarize the main vibe instead of listing every small score component.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

My biggest learning moment was seeing how much the final ranking changes when just one weight changes. A small scoring rule can create very different recommendation behavior. AI tools helped me move faster when I was planning profiles, writing scoring logic, and checking for edge cases, but I still had to double-check the outputs because the tool could suggest ideas that sounded reasonable without matching the assignment exactly. What surprised me most is that even a simple rules-based system can still feel like it "understands" music taste when the inputs are chosen well. If I extended this project, I would try adding user history, diversity rules, and a way to compare collaborative filtering with my current content-based approach.
