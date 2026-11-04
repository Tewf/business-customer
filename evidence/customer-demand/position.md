# Position

Step 4 of the review. What is known, what was not found, and what this repository asks. Each "not found" is a statement about these searches, not about the world. Terms are in [frame](frame.md).

**Shape:** [position](https://github.com/Tewf/reader-ergonomics-review/blob/c43f2770000a9af5c2aa3cbc6f997da7a7e13b34/shapes/position.md)

## Known

- Demand is estimated from choices with random utility models, and free software does it (McFadden 2000, Train 2009, Bierlaire 2026 Biogeme, Croissant 2026 mlogit).
- Stated answers carry errors that are situational: social desirability, satisficing, the order of questions (Tourangeau 2007, Krosnick 1991).
- A change in intention gives a smaller change in behaviour (Webb 2006); an incentive helps a choice study predict purchase (Ding 2005).
- Interviews with a homogeneous group saturate in about 9 to 17 (Hennink 2022).
- A plan fixed before the outcomes protects against hindsight (Nosek 2018).

## Not found in these searches

- A protocol shape for a customer study (strings F26 to F28).
- A trial of a structured protocol against an unstructured round of interviews (strings F19, F22, F23).
- A minimum sample for a choice study of a new good with no prior estimate (strings F2, F8, F9).
- An estimator of unseen themes applied to customer interviews (string F33, not run).
- A test of a segment found by interview against one found by choice (strings F16 to F18).

## The questions

| Question | Answer from the evidence | Grade |
|---|---|---|
| Q1 how many interviews, and an estimator? | about 9 to 17 for a homogeneous segment; a Poisson model and a threshold rule give an estimator of the unseen | measured, descriptive |
| Q2 how far do stated and revealed differ? | d = 0.66 in intention gives d = 0.36 in behaviour; the gap is measured by an observed action after the answer | measured |
| Q3 what does a choice study need? | a design checked against the task-force reports and a power calculation for the coefficients; no rule for a new good | convention |
| Q4 what must a protocol fix? | the question, the sample, the instrument and the analysis plan before the first answer; a program can check that each is declared | convention |

## What this repository asks

- Does a protocol that fixes the sample, the question order and the incentive before the first interview change what a founder concludes from the same customers?
- Do the segments of a round of interviews match the segments of a choice estimate on the same customers?

## What the shapes must decide

- A customer study declares its sample, its question order and its incentive; the shape is [customer-study](../../shapes/customer-study.md) and a program checks the three.
- The analysis plan and the stopping rule are judgment for now, and become checks when a study has used them.
