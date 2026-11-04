# Protocol: how the pool was built

A first pass, run on 2026-11-04 by one reviewer. Terms are in [frame](frame.md).

**Shape:** [protocol](https://github.com/Tewf/reader-ergonomics-review/blob/c43f2770000a9af5c2aa3cbc6f997da7a7e13b34/shapes/protocol.md)

## 1. Why grey literature

Garousi's seven questions: one yes suggests including grey sources.

| Question | Answer |
|---|---|
| Is there a lack of volume or quality in the formal literature? | yes: customer discovery is taught in books, essays and courses that no journal reviewed |
| Is the context important in the outcome? | yes: a founder's practice depends on the tools and the stage |
| Is the goal to corroborate science with practice? | yes |
| Is the goal to challenge assumptions of practice? | yes: whether a few interviews suffice |
| Do practitioners provide most of the information? | yes, for the interview |
| Does the research focus on emerging practice? | yes |
| Is the subject a technology or a tool? | yes: estimation software |

## 2. Questions

- Q1 how many interviews does a segment need, and can an estimator of the unseen say so?
- Q2 how far do stated and revealed answers differ, and how is the gap measured?
- Q3 what does a discrete choice study need in sample and design to estimate demand for a new good?
- Q4 what must a protocol fix before the first question, and what can a program check?

## 3. Existing reviews

- Found: systematic reviews of saturation (Hennink 2022), of the validity of choice experiments (Rakotonarivo 2016), of the hypothetical bias in them (Haghani 2021a), and a history of the customer-development method (Bocken 2019, a commentary).
- Not found: a review that joins interviews, surveys, choice models and pre-orders as evidence for one demand question.
- Willingness to pay and the stated-paid gap on price are held by [business-pricing](https://github.com/Tewf/business-pricing/blob/0d746beca6c5f2395e434ddbbc38c9d5a73d2cb2/evidence/willingness-to-pay/README.md); this review adds the gap on choice and on intention.

## 4. Formal search

Database: OpenAlex, title and abstract, sorted by citations, the top 8 screened. No key, no identity sent. Counts are of 2026-11-04.

| Id | String as run | Count | New concept |
|---|---|---|---|
| F1 | "discrete choice" survey review | 732 | yyynnnny |
| F2 | "discrete choice experiment" "sample size" | 182 | yynyynnn |
| F3 | "hypothetical bias" "stated choice" | 36 | nyyynynn |
| F4 | "discrete choice" "random utility" review | 96 | yynnnnny |
| F5 | McFadden "conditional logit" "qualitative choice" | 5 | nnnnn |
| F6 | "mixed logit" "discrete choice" heterogeneity | 701 | ynnnnn |
| F7 | "discrete choice experiments" "conjoint analysis" difference | 30 | nnnnn |
| F8 | "choice-based conjoint" "sample size" OR "number of respondents" | 1885 | nnnnn |
| F9 | "efficient design" "stated choice experiment" | 20 | ynynnnnn |
| F10 | "social desirability" survey review | 381 | nyyyynnn |
| F11 | "question order" effects survey | 207 | ynnnyyny |
| F12 | "satisficing" survey response cognitive | 75 | yynyynyn |
| F13 | "data saturation" interviews sample size | 604 | yyynynnn |
| F14 | "how many interviews" enough | 27 | nyynnynn |
| F15 | "usability problems" "number of" users mathematical model | 4 | ynyn |
| F16 | "market segmentation" review heterogeneity | 48 | ynynnnnn |
| F17 | "latent class" segmentation choice model | 174 | ynynynny |
| F18 | "market segmentation analysis" methods | 60 | nnnnn |
| F19 | "lean startup" randomized | 7 | ynyynnn |
| F20 | "customer development" startup hypotheses | 18 | nnnnn |
| F21 | "intention-behavior gap" meta-analysis | 23 | ynnynnyn |
| F22 | "scientific approach" "entrepreneurial decision making" randomized | 8 | yynnnnnn |
| F23 | "lean startup" review academic practitioner | 8 | ynnnnn |
| F24 | "lean startup" critique experimentation business model | 2 | yn |
| F25 | "changing behavioral intentions" behavior change meta-analysis | 3 | ynn |
| F26 | "checklist" "conjoint analysis" "good research practices" | 13 | yyynnnnn |
| F27 | "COREQ" OR "consolidated criteria for reporting qualitative research" | 5196 | ynnnnn |
| F28 | "preregistration" revolution | 52 | ynnynnnn |
| F29 | "incentive-aligned" conjoint | 24 | nynnnnyy |
| F30 | "sample sizes for saturation" qualitative systematic review | 4 | ynnn |
| F31 | "controlled experiments" web survey practical guide | 3 | yyn |
| F32 | Felin "lean startup" business model experimentation revisited | not run | not run |
| F33 | estimating the number of unseen themes in interviews, a species estimator | not run | not run |

- F32 and F33 returned HTTP 429 (too many requests) and were not rerun.
- F5 returned nothing useful: the seminal paper is not indexed by its abstract. It was found by title from McFadden 2001 and Train 2009, and F5 counts as a failed query, not as proof it is absent.

## 5. Grey search

| Id | Producer or engine | String or what was read | Result | New concept |
|---|---|---|---|---|
| G1 | an essay by a founder-investor | the page "Do Things that Don't Scale" | included, 1 page read | y |
| G2 | a business magazine | the summary and opening of the article on the lean start-up | included, 1 page read | y |
| G3 | the site of a handbook on customer conversations | the front page | included, 1 page read | y |
| G4 | the site of the lean start-up method | the page of principles | included, 1 page read | y |
| G5 | a usability consultancy | the article on testing with 5 users | included, 1 page read | y |
| G6 | a product-coaching site | the page on the interview snapshot | included, 1 page read | y |
| G7 | a university laboratory | the home page of the estimation package Biogeme | included, 1 page read | y |
| G8 | the R archive CRAN | the page of the package mlogit | included, 1 page read | n |
| G9 | the site of a book on online experiments | the front page | included, 1 page read | y |
| G10 | the Apollo choice-modelling site | the home page | not read: a bot check answered | not run |
| G11 | a survey-research association | its code of ethics page | not read: HTTP 403 | not run |
| G12 | a preregistration service | its home page | not read: HTTP 403 | not run |
| G13 | a conjoint-software vendor | a technical paper on sample size | not read: the page held no paper | not run |
| G14 | a strategy-tools vendor | a page on testing ideas | not read: HTTP 404 | not run |

- A bot check was not passed, and no identity was supplied. A source reachable only that way is unverifiable.

## 6. Stopping rule

- Effort bounded and saturation, stated before the search: the top 8 results per string by citations (N = 8), and a string stops after 5 consecutive results that add no concept (k = 5).
- The grey pages were chosen by the reviewer from the practice named in [frame](frame.md), one page each, with no ranking by an engine.

## 7. Selection

- Include: a work that measures, defines or requires something about interviews, surveys, choice models, field experiments or segmentation, or that a practice guide cites as its method.
- Exclude: an application of a method to a single good, a clinical or environmental result with no method content, and a work that duplicates a pricing finding.
- Quality: a grey source scoring under 10 of 20 is an example of practice only.

## 8. Quality of grey sources

Garousi's 20 criteria in eight groups: authority 4, methodology 6, objectivity 4, date 1, position 1, novelty 2, impact 1, outlet 1. The threshold is 10 of 20. Scores are in [sources](sources.md).

## 9. Extraction and synthesis

- An abstract was read for each formal source with a figure; a figure from an abstract is marked (secondary) in [review](review.md).
- A work whose abstract the index did not hold is located only, and no figure is taken from it.
- Synthesis is narrative by question, traceable through [sources](sources.md).

## 10. Not searched, and limits

- Not searched: databases other than OpenAlex; Google Scholar; books by publisher; forums and podcasts; the law of consent in surveys.
- Not searched: survey weighting and nonresponse adjustment beyond the cited reviews; conjoint types such as best-worst scaling.
- Limits: one reviewer and no second rater; the New concept letters are the reviewer's own call; OpenAlex returns by citations, which favours old work.
- A page that answered a bot check or an error was not read, and its absence says nothing about the practice it holds.
