# Stableford Scoring in Golf

A beginner-friendly guide to understanding Stableford scoring, how it differs from traditional stroke play, and how to calculate your points using your course handicap, slope rating, and the hole stroke index.

---

## Contents

1. [What Is Stableford Scoring?](#what-is-stableford-scoring)  
2. [Stableford Points Table](#stableford-points-table)  
3. [Course Handicap, Slope Rating & Stroke Index](#course-handicap-slope-rating--stroke-index)  
4. [How to Calculate Your Stableford Score](#how-to-calculate-your-stableford-score)  
5. [Real-World Example](#real-world-example)  
6. [Key Takeaways](#key-takeaways)

---

## What Is Stableford Scoring?

Stableford is a scoring system in golf that awards points **per hole** based on your score relative to par, rather than counting total strokes.  

- **Traditional stroke play** tallies every stroke over 18 holes; lowest total wins.  
- **Stableford** awards points on each hole; only positive contributions count toward your total.  
- If you score poorly on a hole, you can pick up once no points are possible, speeding up play.

---

## Stableford Points Table

| Score vs. Par            | Points Earned |
|--------------------------|--------------:|
| **Double bogey (or worse)** | 0             |
| **Bogey (+1)**           | 1             |
| **Par (E)**              | 2             |
| **Birdie (–1)**          | 3             |
| **Eagle (–2)**           | 4             |
| **Albatross (–3)**       | 5             |

---

## Course Handicap, Slope Rating & Stroke Index

### Slope Rating

- **Slope Rating** measures course difficulty for a bogey golfer relative to a scratch golfer (e.g., 120). It's printed once for the entire course.

### Course Handicap

Converts your Handicap Index into the strokes you receive on that course:

\[
\text{Course Handicap} = \left(\frac{\text{Handicap Index} \times \text{Slope Rating}}{113}\right) + (\text{Course Rating} - \text{Par})
\]

- **Handicap Index**: your playing ability (e.g., 18.2).  
- **Course Rating**: expected score for a scratch golfer (e.g., 72.0).  
- **Slope Rating**: difficulty for a bogey golfer (e.g., 120).  
- **Par**: total par for the course (e.g., 72).

### Stroke Index

Each hole is ranked 1 (hardest) to 18 (easiest) on the scorecard:

| Hole       | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|-----------:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Par**    | 4  | 5  | 3  | 4  | 4  | 5  | 3  | 4  | 4  | 4  | 3  | 4  | 4  | 5  | 3  | 4  | 4  | 4  |
| **Stroke Index** | 1  | 9  | 15 | 3  | 11 | 7  | 17 | 5  | 13 | 2  | 10 | 6  | 14 | 4  | 16 | 18 | 8  | 12 |

Your **Course Handicap** determines where you get strokes:
- If your course handicap is **19**, you receive 1 stroke on all holes (indexes 1–18) plus an extra stroke on the hole with index 1.

---

## How to Calculate Your Stableford Score

1. **Determine your Course Handicap.**  
2. **Apply handicap strokes** to each hole based on its Stroke Index.  
   - Subtract strokes received from gross score to get your **net score**.  
3. **Convert net score to Stableford points** (see points table).  
4. **Sum all points** over 18 holes for your total Stableford score.

---

## Real-World Example

**Player Profile**  
- Handicap Index: **18.2**  
- Course Rating: **72.0**  
- Slope Rating: **120**  
- Par: **72**

### Step 1: Calculate Course Handicap

\[
\text{Course Handicap} = \frac{18.2 \times 120}{113} + (72.0 - 72) \approx 19.3 \;\Rightarrow\; \mathbf{19}
\]

### Step 2: Strokes Received by Hole

| Hole | Par | Stroke Index | Strokes Received |
|-----:|----:|-------------:|-----------------:|
| 1    | 4   | 1            | 2                |
| 2    | 5   | 9            | 1                |
| 3    | 3   | 15           | 1                |
| 4    | 4   | 3            | 1                |
| 5    | 4   | 11           | 1                |
| 6    | 5   | 7            | 1                |
| 7    | 3   | 17           | 1                |
| 8    | 4   | 5            | 1                |
| 9    | 4   | 13           | 1                |
| 10   | 4   | 2            | 1                |
| 11   | 3   | 10           | 1                |
| 12   | 4   | 6            | 1                |
| 13   | 4   | 14           | 1                |
| 14   | 5   | 4            | 1                |
| 15   | 3   | 16           | 1                |
| 16   | 4   | 18           | 1                |
| 17   | 4   | 8            | 1                |
| 18   | 4   | 12           | 1                |

### Step 3: Hole‑By‑Hole Scoring

| Hole | Par | Gross Score | Strokes Received | Net Score | Net vs Par   | Stableford Points |
|-----:|----:|------------:|-----------------:|----------:|-------------:|------------------:|
| 1    | 4   | 6           | 2                | 4         | Par          | 2                 |
| 2    | 5   | 6           | 1                | 5         | Par          | 2                 |
| 3    | 3   | 6           | 1                | 5         | +2 (Double) | 0                 |
| 4    | 4   | 4           | 1                | 3         | -1 (Birdie) | 3                 |
| 5    | 4   | 4           | 1                | 3         | -1 (Birdie) | 3                 |
| 6    | 5   | 8           | 1                | 7         | +2 (Double) | 0                 |
| 7    | 3   | 3           | 1                | 2         | -1 (Birdie) | 3                 |
| 8    | 4   | 5           | 1                | 4         | Par          | 2                 |
| 9    | 4   | 6           | 1                | 5         | +1 (Bogey)  | 1                 |
| 10   | 4   | 5           | 1                | 4         | Par          | 2                 |
| 11   | 3   | 4           | 1                | 3         | Par          | 2                 |
| 12   | 4   | 6           | 1                | 5         | +1 (Bogey)  | 1                 |
| 13   | 4   | 4           | 1                | 3         | -1 (Birdie) | 3                 |
| 14   | 5   | 6           | 1                | 5         | Par          | 2                 |
| 15   | 3   | 5           | 1                | 4         | +1 (Bogey)  | 1                 |
| 16   | 4   | 4           | 1                | 3         | -1 (Birdie) | 3                 |
| 17   | 4   | 3           | 1                | 2         | -2 (Eagle)  | 4                 |
| 18   | 4   | 3           | 1                | 2         | -2 (Eagle)  | 4                 |

### Step 4: Total Stableford Score

Sum the “Stableford Points” for all 18 holes:

> **Example Total:** 38 points

This player scored **38 Stableford points**, a very strong round (above the typical 36‑point benchmark).

---

## Key Takeaways

- Stableford keeps every hole interesting and speeds up poor holes.  
- **Slope Rating** influences your Course Handicap; **Stroke Index** shows where you apply strokes.  
- Calculate **net score** (gross minus strokes received), then convert to Stableford points.  
- A mid‑handicap benchmark is **36 points**; this example shows a **38‑point** round.

*Enjoy your next Stableford round!*

https://owltourism.com/uploads/The-Pasha-EGA-Handicap-Slope-Rating.pdf
https://owltourism.com/uploads/Lykia-Slope-Rating-Playing-Handicap.pdf
https://owltourism.com/uploads/PGA-Sultan-EGA-Handicap-Slope-Rating.pdf
https://owltourism.com/uploads/Nobilis-Scorecard.pdf