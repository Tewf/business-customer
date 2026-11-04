# 0002: Keep the name, and let a program read a study protocol

**Decision:** The repository keeps its name after the frame step. The baseline of its first review is B1, a protocol-fixed study with a choice arm against an unstructured round of interviews, and a program checks that a study declares its sample, question order and incentive.

**Status:** accepted, 2026-11-04. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a/shapes/decision-record.md).

## Context

- The frame step found the field's words: discrete choice analysis for demand, survey methodology for the asking, and customer discovery in practice ([frame](../evidence/customer-demand/frame.md)).
- The review found no protocol shape for a customer study, and no trial of one against unstructured interviews ([position](../evidence/customer-demand/position.md)).
- Interviews saturate near 9 to 17 for a homogeneous group, intention moves behaviour less than itself, and a plan fixed before the outcomes is the field's remedy for hindsight ([review](../evidence/customer-demand/review.md)).
- The review is finished only when it names a baseline.

## Decision

- Keep the name. The field splits what the name joins, but the two halves meet in one question: what a study must fix before the sale.
- Name the baseline B1 ([baseline](../evidence/customer-demand/baseline.md)).
- Write a shape, [customer-study](../shapes/customer-study.md), and a check, `customer-study`, that fails a protocol with no sample size, no numbered question order or no incentive with its payer.
- Leave the analysis plan and the stopping rule to judgment until a study has used them.

## Consequences

- A reader can compare any customer study with B1 and with the studies that bear on each of its parts.
- A study that hides the sample, the order or the incentive fails a program, not a reader's memory.
- **Bad:** the check reads three declarations and not their quality; a representative sample and an unbiased order stay judgment.
- **Bad:** B1 is first run on simulated data and a fixture, so it has met no customer.
- **Bad:** twelve works are located only and five pages could not be read, so some figures rest on abstracts ([against](../evidence/customer-demand/against.md)).

## See also

[Decisions](README.md); [baseline](../evidence/customer-demand/baseline.md); [record 0001](0001-a-repository-of-its-own.md).
