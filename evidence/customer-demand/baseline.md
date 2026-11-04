# Baseline

Step 5 of the review: the baseline the work is compared against. Evidence is in [review](review.md).

**Shape:** [baseline](https://github.com/Tewf/reader-ergonomics-review/blob/c43f2770000a9af5c2aa3cbc6f997da7a7e13b34/shapes/baseline.md)

## B1: a protocol-fixed study with a choice arm, against an unstructured round of interviews

1. Write the study in the [customer-study](../../shapes/customer-study.md) shape: sample, question order and incentive declared, and the analysis and stopping rule, before the first interview.
2. Arm A, the practice: an unstructured round of interviews on past behaviour, coded by theme, stopped by a threshold rule fixed in the protocol.
3. Arm B: a discrete choice experiment, designed to the task-force reports, sized by a power calculation, estimated by a conditional logit in Biogeme or mlogit. It is run first on simulated data with known parameters, to show the estimate recovers them.
4. Compare the arms on the same segments, and add a paid action on the price side as in [business-pricing's baseline](https://github.com/Tewf/business-pricing/blob/0d746beca6c5f2395e434ddbbc38c9d5a73d2cb2/evidence/willingness-to-pay/baseline.md).

The practice in arm A is the one the customer-development guides describe (Blank 2013, Fitzpatrick 2013, Torres 2024).

## Compared with what the review found

| Item | In B1 | Fit |
|---|---|---|
| A plan fixed before the outcomes (Nosek 2018) | the protocol declares them | matches |
| A reporting checklist (Tong 2007) | the shape asks its three domains in part | in part |
| A design and analysis plan for choice (Bridges 2011, Johnson 2013, Hauber 2016) | arm B follows them, reports located only | in part |
| A power calculation (de Bekker-Grob 2015) | arm B is sized by it | matches |
| An incentive on the answer (Ding 2005) | declared in the protocol; real stakes only on the price side | in part |
| A stopping rule for interviews (Guest 2020, Nielsen 1993) | arm A uses a threshold rule | matches |
| Segments with heterogeneity (Kamakura 1996, McFadden 2000) | arm B tests a mixed logit against the plain one | in part |
| A gap between intention and behaviour (Webb 2006) | an observed paid action after the answer | in part |

## What B1 lacks

- A trial of a protocol against an unstructured round; B1 only compares two arms on one study (position, Not found).
- Real customers: the first run is simulated data and a fixture.
- A minimum sample for a new good (position, Not found).
- A test that the interview segments match the choice segments (position, Not found).
- Saturation evidence for heterogeneous groups, which need more interviews (Hennink 2022).

## How it is measured

- Recovery: the mean absolute error of each estimated coefficient on simulated data with known values.
- Agreement: the rank correlation of the segments' demand between arm A and arm B.
- Saturation: the share of new themes in the last interviews of arm A, against the estimate of the unseen.
- The gap: the effect size of the stated intention on the paid action, as d.
- A repeat: the check `customer-study` runs on any protocol, and its tests pass on a fixture with no real respondent.

## The review is finished

The baseline is named: B1. The next work is a design document that fixes the first good, the segments and the arms.
