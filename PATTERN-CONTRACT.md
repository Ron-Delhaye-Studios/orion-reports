# PATTERN CONTRACT — ORION × FORTUNA shared event timeline

One table, two lenses. ORION writes geopolitical events; FORTUNA writes
market events. Both write to the same `events` table so a single timeline
holds both kinds of signal. The `event_links` table expresses how they
relate. The patterns between them are the product.

## Who writes what

| origin    | writer   | content                                              |
|-----------|----------|------------------------------------------------------|
| `orion`   | ORION    | Geopolitical events: summits, sanctions, conflicts,  |
|           |          | elections, policy shifts, narrative outbreaks.       |
| `fortuna` | FORTUNA  | Market events: sharp moves, whale footprints, regime |
|           |          | shifts, trim/reseed tripwires, liquidity shocks.      |

Neither LDI writes the other's event type. If a market move looks
geopolitical, FORTUNA files the market event and ORION links the
geopolitical trigger — the link is the claim, and it carries the evidence.

## Source grading (both writers, no exceptions)

- `confirmed` — independently corroborated by multiple credible sources.
- `single-source` — one credible source; treated as provisional.
- `narrative` — widely repeated but unverified, or editorial framing
  presented as fact somewhere. Labeled, never laundered.

An event's grade can be upgraded only by new evidence, never by
repetition. The `sources` JSONB column holds the receipts.

## Link types

- `trigger` — "this headline moved that market." Directional:
  from the geopolitical event → to the market event. The `note` must say
  what the evidence is (timing, magnitude, mechanism), not just that both
  happened.
- `convergence` — separate events pointing the same direction. No claim
  that one caused the other — only that the pattern is louder together.
- `origin` — where a narrative was born and how it traveled. From the
  earliest traced instance → to later echoes.

## Reading the board

The pattern board answers, in order:

1. **What happened?** — the events, graded.
2. **Where did it originate?** — the origin links.
3. **How did it converge?** — the convergence links.
4. **Who's connected?** — actors and regions shared across linked events.

Correlation is not causation until a `trigger` link earns it with
evidence. That discipline is the whole edge over a news aggregator.

## Technical notes

- Schema: see the Supabase SQL for `events` / `event_links` (sibling file
  `supabase-orion-schema.sql`, kept with the operator, not in this repo).
- Public reads go through the aggregate function `get_event_feed()` —
  recent events with grade counts. Raw `sources` are not publicly
  exposed.
- RLS: anon INSERT-only. Writes are attributed by the `origin` column;
  each LDI writes only its own origin value.
