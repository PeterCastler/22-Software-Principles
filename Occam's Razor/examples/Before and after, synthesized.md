# Before and after

## Before: assumptions multiplied

A five-person product team needs an internal approval application. The proposed architecture contains three independently deployed services, a message broker, distributed tracing, eventual-consistency repair jobs, and separate databases because the product *may* later serve millions of users.

## After: assumptions removed

Start with one deployable application and one transactional database. Keep approval rules and notification effects in clear modules. Split a component only after measured scaling, ownership, release-cadence, or isolation requirements justify the operational boundary.

The after design is not “monoliths are always best.” It simply declines to assume future scale, organizational independence, and asynchronous consistency before evidence exists.
