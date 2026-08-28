# Source Boundary

This directory identifies the immutable evidence substrate used to build the machine-readable KJV corpus.

The governing relation is:

```math
\boxed{
\text{canonical verse}
\leftrightarrow
\text{exact pinned source bytes}
\leftrightarrow
\text{deterministic extraction}
}
```

The current source pin is recorded in [`PINNED_SOURCE.json`](PINNED_SOURCE.json).

## Important distinction

```math
\boxed{\text{verse ID} \neq \text{evidence}}
```

`GEN.1.1` is an address. Evidence is the value recovered from the pinned source snapshot and bound to its source-file fingerprint and verse-text hash.

The current source is an immutable Git snapshot rather than a moving branch name:

```text
repository: renniemaharaj/kjv-bible
commit:     88723a44bb3e3f229a34f9cf11ce1b7acf971eee
tree:       df15756d8f2922f24c36ec86081d4d3244277619
```

The upstream repository describes its corpus as 66 books / 1,189 chapters / 31,102 verses and publishes a deterministic whole-corpus SHA-512 fingerprint. `ml-didacticism` pins that exact snapshot; it does not promote the upstream label or verification history into independent bibliographical authority.

## Byte identity versus textual authority

A matching commit/tree/fingerprint establishes that two copies contain the same pinned bytes.

It does **not** establish, by hashing alone, that those bytes are the uniquely correct KJV wording or the uniquely correct historical edition.

That distinction is intentional:

```math
\boxed{
\text{byte identity}
\neq
\text{bibliographical authority}
}
```

## Materialization

The source bytes can be materialized by checking out the pinned upstream commit. The deterministic ingester then verifies the 66-book corpus fingerprint before extracting any verse.

No structural or interpretive output is allowed to modify this source pin.
