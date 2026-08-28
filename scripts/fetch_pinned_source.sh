#!/usr/bin/env sh
set -eu

REPO_URL="https://github.com/renniemaharaj/kjv-bible.git"
COMMIT="88723a44bb3e3f229a34f9cf11ce1b7acf971eee"
TREE="df15756d8f2922f24c36ec86081d4d3244277619"
DEST="${1:-source/upstream/kjv-bible}"

if [ -e "$DEST" ]; then
  echo "error: destination already exists: $DEST" >&2
  exit 1
fi

git clone --no-checkout "$REPO_URL" "$DEST"
git -C "$DEST" checkout --detach "$COMMIT"

ACTUAL_COMMIT=$(git -C "$DEST" rev-parse HEAD)
ACTUAL_TREE=$(git -C "$DEST" rev-parse 'HEAD^{tree}')

if [ "$ACTUAL_COMMIT" != "$COMMIT" ]; then
  echo "error: commit mismatch: $ACTUAL_COMMIT" >&2
  exit 1
fi

if [ "$ACTUAL_TREE" != "$TREE" ]; then
  echo "error: tree mismatch: $ACTUAL_TREE" >&2
  exit 1
fi

printf '%s\n' "Pinned source materialized at $DEST"
printf '%s\n' "commit: $ACTUAL_COMMIT"
printf '%s\n' "tree:   $ACTUAL_TREE"
