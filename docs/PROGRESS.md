# PROGRESS - Spotify-Profile-Github

Updated: 2026-11-12 by Codex. Timeline fix published as `3e5f70d412d121c1edd6c9e2b64a5685d3c51154`.

## In progress

- The user approved pushing the timeline fix and selected version `V1.0.1`. Master and the annotated tag were pushed atomically. The tag currently resolves to `3e5f70d`; `V1.0.0` remains at `31bdbc7`.
- Release ID `442704488` was changed externally from V1.0.0 to V1.0.1 during publication. Its title and notes were updated after checking its ID and update timestamp. Release: https://github.com/LienThuan04/Spotify-Profile-Github/releases/tag/V1.0.1
- The user then requested English project content. Release notes and this task's documentation additions are now English; AGENTS.md records the preference. English-only additions and whitespace checks passed. A follow-up commit will be pushed and V1.0.1 will be moved to that final commit with a lease protecting the current tag.
- GitHub Wiki was synchronized at `956a583`: only the Mini size and shared timeline description changed in Home.md; other Wiki pages were preserved.

## Verified implementation

- All 15 themes now share a CSS progress bar and elapsed clock; eight previously unsupported themes were fixed. The bar and clock stop together. Recent tracks remain static, offline cards hide the timeline, and missing timing never animates. Apple/Embed use real elapsed and total times.
- Mini is 96px tall (72px offline). Five classic themes gain 33px when a timeline is visible. Only make_svg and templates changed at runtime; fetching, caching, Firestore, and original symlinks are unchanged.
- Full tests before publication: 706 pytest passed in 2.40s, 11 Node tests passed, and 105 SVG previews validated. Independent review found no issues and ran 602 view tests. AST comparison and git diff checks passed.
- Preview: `graphify-out/timeline-review/index.html`. Runner: `.venv/Scripts/python.exe graphify-out/timeline-review/verify.py`; logs: `pytest.log`, `pytest.xml` in the same directory. Windows tests use a temporary snapshot that resolves the two Git symlink stubs.
- Graph refresh succeeded outside the sandbox: 545 nodes, 772 edges, 38 communities. CUA inventory was empty; actual browser geometry, animation, and deployment remain unverified.
- GitHub REST authentication requires `username=LienThuan04` in credential fill. Omitting it failed because prompting was disabled; the existing account credentials work without a new login. Never print or persist the returned token.

## Next step

Commit and push the English documentation correction, update V1.0.1 to that commit, publish English release notes, sync the changed Wiki page, and verify all remote refs and release metadata.

## Journal

- 2026-11-12 - Codex - User requested English project content after publication; translating this task's additions and updating the language rule.
- 2026-11-12 - Codex - Published timeline fix 3e5f70d and V1.0.1; 706 pytest, 11 Node, 105 SVG previews passed; no independent review findings.
