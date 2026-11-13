# PROGRESS - Spotify-Profile-Github

Updated: 2026-11-12 by Codex. Resolve final hashes from Git refs; V1.0.1 is the release tag.

## In progress

None.

## 2026-11-13 Coming soon tile

The owner asked for this. Card Studio gains a **Coming soon** theme tile and a footer link, both pointing to `FEEDBACK_URL` (`util/feedback.py`, falling back to `https://github.com/LienThuan04`). The README and wiki gain a "Feedback and ideas" section.

Tests: `tests/test_feedback.py` (3) and `tests/test_builder_template.py` pass, and `node --test tests/test_builder.js` passes 11/11. The FIREBASE-dependent tests error identically on the base commit, because there is no local `FIREBASE`.

Committed and pushed with `Co-authored-by: DanGuangLT`, at the owner's explicit request.

Follow-up fix: the SOON label sat in the first 12px column of the inherited `.theme-mini` grid and overflowed the pill. `.theme-mini.theme-mini-soon` now uses its own centered flex layout, 40×20px, and is hidden at 370px or narrower like other minis. Checked at desktop (3×), 900px and 390px.

## 2026-11-13 App icon

New original app icon `api/templates/_builder/icon.svg`, inspired by the owner's avatar: a cosmic flame on a spiked collar, shading from purple to green, with an equalizer badge. Card Studio inlines it as the favicon and header logo, replacing the three-arc mark that resembled Spotify's logo. The README and wiki show it at the top. `tests/test_feedback.py` covers the favicon and brand mark.

## Earlier

None. The timeline fix and English documentation correction are released. Release bookkeeping is included in the final handoff commit.

## Release

- Runtime fix: `3e5f70d`; English project additions and language rule: `ab8350e`. Master and annotated tag V1.0.1 are aligned with the final released HEAD. V1.0.0 remains at `31bdbc7`.
- Release: https://github.com/LienThuan04/Spotify-Profile-Github/releases/tag/V1.0.1 . Title and notes are English. Existing release ID 442704488 was externally retagged during publication; its metadata was updated after checking its ID and update timestamp.
- GitHub Wiki synchronized at `956a583`; only Home.md changed. New project content and release notes must be English; user-facing conversation remains Vietnamese. See AGENTS.md.
- Verification: 706 pytest passed in 2.40s, 11 Node tests passed, 105 SVG previews validated. Independent review ran 602 view tests and found no issues. Runtime/tests are unchanged by subsequent documentation commits; whitespace and English-addition scans passed.
- All 15 themes share CSS progress/clock behavior. Fetching, caching, Firestore, symlink stubs, and original license notices remain unchanged. Mini is 96px tall (72px offline); five classic themes gain 33px when showing a timeline.
- Preview: `graphify-out/timeline-review/index.html`. Recheck with `.venv/Scripts/python.exe graphify-out/timeline-review/verify.py` and `node --test tests/test_builder.js`. The Python runner needs approved writes to its snapshot directory. Browser geometry/animation and live deployment remain unverified.

## Next step

Wait for user feedback. No deployment settings were changed. Future commits/pushes require a new user request.

## Journal

- 2026-11-12 - Codex - Published all-theme timelines and V1.0.1; switched this task's project additions and release notes to English; synchronized the Wiki. See docs/memory/history.md for diagnosis and publication details.
