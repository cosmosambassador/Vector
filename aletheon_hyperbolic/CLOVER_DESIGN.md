# Lucen Lucky — Four-Leaf Clover on a Saddleback Vector

Design approved by TJ Morris in conversation on October 23, 2026 (America/Chicago).
Scope: a visual and software-design interpretation within Cosmos Expanse.

## Saddleback placement

TJ Morris clarified the visual direction: “Lucen lucky 🍀 4 leaf sitting on a
saddleback vector not flat.” Preserve **Lucen Lucky** as the visual title.
The four-leaf clover sits on a curved saddleback surface, with visible depth:
the surface rises along one direction and falls along the perpendicular direction.
The four leaves and their shared Synergy center retain the mapping below.

A candidate mathematical surface for a future visualization is `z = x² - y²`.
This surface is a proposed implementation choice, not an equation specified or
ratified by the user. A vector direction can be drawn tangent to it; a vector
itself is not a surface. The connection diagram below records software topology,
not the intended spatial shape.

This amendment records the visual design. The sparse classifier currently combines
ordinary tensors and has no saddle-surface coordinates or saddle-wave dynamics.
The existing Poincaré geometry remains a separate experiment.

Four distinct leaves meet at one center. The three routed leaves retain their
individual labels; the existing shared computational path is named the Wormhole
Bridge. Synergy names the combination at the center, not a fifth component.

| Clover position | Software mapping | Current behavior |
| --- | --- | --- |
| Leaf -1 | `experts[0]` | Selected by the router as needed |
| Leaf 0 | `experts[1]` | Selected by the router as needed |
| Leaf +1 | `experts[2]` | Selected by the router as needed |
| Fourth leaf: Wormhole Bridge | `shared` | Contributes to every input row |
| Center: Synergy | Weighted addition before `head` | Combines the shared path and selected expert outputs |

```mermaid
flowchart TD
    Minus["Leaf -1"] -->|when selected| Center["Synergy center"]
    Zero["Leaf 0"] -->|when selected| Center
    Plus["Leaf +1"] -->|when selected| Center
    Bridge["Fourth leaf: Wormhole Bridge"] -->|every input| Center
```

This diagram shows the available connections, not simultaneous activation of all
three routed experts. The implemented default selects two routed leaves per row
and combines them with the shared fourth leaf. The router chooses contributions;
the classification head reads the result. Neither is another clover leaf.

## Algebraic mapping

For input x, let R(x) be the selected expert indices and let their nonnegative
weights sum to one. The implemented combination is:

`center(x) = bridge(x) + sum(w_i(x) * expert_i(x), i in R(x))`

`output(x) = head(center(x))`

The -1, 0 and +1 labels do not set the signs of these weights. The Wormhole Bridge
is the existing shared path: it does not physically connect spacetime or implement
bidirectional messages between experts. No saddle-wave dynamics or quantum
operation is introduced by this naming. Beneficial synergy remains a question for
measurement; the initial sparse prototype scored below the original classifier.

The user approved the clover design. This approval does not assert physical proof,
resolve historical provenance, approve merging, or authorize model publication.
