# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

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

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
