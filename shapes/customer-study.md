# Shape: customer study

The protocol of one study of customers, written before the first interview or survey. Its reader is whoever must trust or repeat the study, and asks: who was asked, in what order, for what reward, and what was decided before the answers came? It is a page.

## Skeleton

```markdown
# Customer study: <the question, in a few words>

<One sentence: what the study decides, and what it will not decide.>

**Shape:** [customer study](<path to shapes/customer-study.md>)

## Question

<The question the study answers, and the decision that depends on the answer.>

## Sample

- Frame: <who can be asked, as a list or a rule>.
- Recruitment: <how they are reached, and who is not>.
- Size: N = <number>, <why that number>.

## Instrument

<Interview guide, survey or choice task, with the attributes and levels if a choice task.>

## Question order

1. <The first question, asked before any mention of the idea.>
2. <The second question.>

## Incentive

<What a respondent gets, and who pays it; or "None" and who pays nothing.>

## Analysis plan

<How the answers are coded or estimated, fixed before they are seen.>

## Stopping rule

<When the study stops, stated before the first answer.>

## Limits

<What the study cannot say, and the bias it expects.>
```

## Where each part comes from

| Part | Evidence | Grade |
|---|---|---|
| The question and its decision | an analysis plan fixed before the outcomes separates prediction from postdiction (Nosek 2018) | convention |
| Sample frame, recruitment and size | saturation at 9 to 17 interviews for homogeneous samples (Hennink 2022); a power calculation for choice data (de Bekker-Grob 2015) | measured, descriptive; convention |
| Question order | respondents read questions by the norms of conversation (Krosnick 1999); order effects are named in survey methodology, not measured here | supported with caveat |
| Incentive | an incentive on the choice improved the prediction of purchase (Ding 2005); an intention moves behaviour less than itself (Webb 2006) | measured |
| Analysis plan and stopping rule | the same plan-first argument (Nosek 2018); a threshold rule for saturation (Guest 2020) | convention; supported with caveat |
| Limits and reporting | a reporting checklist for interviews (Tong 2007) | convention |

## Worked example

- Ours, a fixture with no real respondent: [pre-order-interviews/study.md](examples/pre-order-interviews/study.md).

## The rules

1. The Sample section gives a frame, a recruitment and a size as N = a number.
2. The Question order section is a numbered list of at least two questions, in the order asked.
3. The Incentive section says what is given, or none, and who pays.
4. The study is dated and committed before its first answer; a later change is a new version with the reason.
5. A study states what it will not decide.

## The principles it applies

| Part | Principle |
|---|---|
| The three declarations first, as headings | [signal the structure](https://github.com/Tewf/reader-ergonomics/blob/722cfa4b0ad65968e2c7e6fdc07057c9bab0e172/principles/page/signal-the-structure.md) |
| One section, one fact | [one place per fact](https://github.com/Tewf/reader-ergonomics/blob/722cfa4b0ad65968e2c7e6fdc07057c9bab0e172/principles/collection/one-place-per-fact.md) |
| The question before the method | [overview first](https://github.com/Tewf/reader-ergonomics/blob/722cfa4b0ad65968e2c7e6fdc07057c9bab0e172/principles/document/overview-first.md) |

## Checked by

`customer-study` (exact), in `checks/local/customer_study.py`, reads each file named in `[customer_study] files` of the config.

- Sample: N = a number, a frame and a recruitment.
- Question order: a numbered list of two or more.
- Incentive: what is given, or none, and who pays.

Whether the sample represents the customers, the order is unbiased and the incentive compatible is judgment.
