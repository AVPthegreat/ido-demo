# ido-demo

A small, made-up shop codebase used to show how [Ido](https://github.com/apps/ido-review-g66) reviews pull requests.
Ido is an AI pull-request reviewer that stays quiet unless it can point at a real bug.

Each branch below is one demo case. Its PR is left open on purpose so the review can be shown; none of them is meant to be merged.

| Branch | PR | What it contains | What Ido should do |
|---|---|---|---|
| `demo/discount-check` | #2 | `best_discount` loops from index 1, so the first coupon is never tried (off-by-one) | One comment on that line, with the fix (`for c in coupons`) |
| `demo/clean-shipping` | #3 | `shipping_fee` with tests; the code is correct | Nothing. Silence is the expected result |
| `demo/live-cart` | (none yet) | `cart_total` ignores quantity, and `free_delivery` uses `>` where reaching the threshold should count | Comments on the real bugs only |
| `feature/invoice-helpers` | #1 | Several planted problems at once: SQL built from user input, a shell command built from input, an off-by-one loop, a hard-coded demo key | Comments on each real problem; no style nits |

All keys and data in this repo are fake.

## Using it in a video or a live demo
1. Open PR #2 and show Ido's single comment: the line, why it breaks, and the fix.
2. Open PR #3 and show that Ido posted nothing on correct code.
3. Optionally, open a PR from `demo/live-cart` live and wait for the review.

## Running the tests
```
python3 -m pytest tests/
```
