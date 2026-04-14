# Evaluation Reflection

## Profiles Tested

- High-Energy Pop
- Chill Lofi
- Deep Intense Rock
- Conflicted Edge Case

## Pairwise Comparisons

- High-Energy Pop vs Chill Lofi: The pop profile pushed upbeat, danceable songs like `Sunrise City` and `Gym Hero` to the top, while the lofi profile preferred softer and more acoustic tracks like `Library Rain` and `Midnight Coding`. This makes sense because the energy and acousticness targets are very different.
- High-Energy Pop vs Deep Intense Rock: Both profiles liked high-energy songs, but the rock profile moved `Storm Runner` to first place because it matched both `rock` and `intense`. The pop profile still favored brighter songs because `happy` and high valence mattered more there.
- High-Energy Pop vs Conflicted Edge Case: The pop profile produced results that felt cohesive, but the edge case profile mixed together songs that matched only one part of the request. That difference shows the recommender handles clear preferences better than contradictory ones.
- Chill Lofi vs Deep Intense Rock: These profiles had the biggest contrast. Lofi results were low-energy, calm, and acoustic, while rock results were loud, intense, and less acoustic, which shows the scoring logic is sensitive to directionally opposite vibes.
- Chill Lofi vs Conflicted Edge Case: Both profiles gave some weight to acousticness, but the lofi profile still produced more natural recommendations because its genre, mood, and energy targets aligned with each other. The edge case profile exposed how hard it is for a simple scoring system to satisfy conflicting signals at once.
- Deep Intense Rock vs Conflicted Edge Case: Both profiles asked for high energy, so songs like `Storm Runner` and `Iron Horizon` still appeared high for the edge case profile. The difference is that the edge case also pulled in `Quiet Constellations` because the exact `classical` match was strong, even though the overall vibe was not very intense.

## Experiment Reflection

- When I doubled the importance of energy and cut genre weight in half, `Rooftop Lights` moved above `Gym Hero` for the High-Energy Pop profile. That happened because `Rooftop Lights` had a better overall energy and mood fit, while `Gym Hero` was relying more on the exact pop genre match.
- The experiment made the results feel a little more flexible, but it also let near-energy matches from other genres rise more easily. That tradeoff suggests the model needs a balance between exact categorical matches and continuous feature similarity.
