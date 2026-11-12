# Project history

## Earlier work - archived on 2026-11-12

- Established the independent repository at `https://github.com/LienThuan04/Spotify-Profile-Github`, branch `master`. The original upstream MIT notice remains in `THIRD_PARTY_NOTICES.md`; displayed attribution is `LianHarman(LienThuan04)`.
- Early commits: root `64f5304`, documentation `2cd1a79`, Spotify layouts `ba38dde`, and simulated 3D equalizers `b337d19`. A full-history bundle was verified before the repository history was replaced.
- Added Spotify card/bar/album layouts, shared CSS macros, six equalizer styles, and local SVG previews. The initial expanded suite passed 204 tests. Seven classic themes and Spotify fetching/caching were preserved at that stage.
- Added iso/ribbon/floor equalizers and Card Studio controls. Card Studio generates URL, Markdown, and HTML embeds with theme-aware options, cover-derived colors, debounced previews, copy tabs, and reset behavior.
- README verification checked 31 image URLs across three playback states (93 valid SVG files) and 14 anchors; the suite then passed 213 tests. Browser/live checks were unavailable.
- Commit `a84746d9e1d1597e864098e79a56af1f74b29c2b` was published through the GitHub connector after direct Git networking failed. Blob uploads followed by a SHA-based tree avoided a connector protocol error. The remote tree matched the staged local tree. Reconstructing the remote commit required preserving its original +0700 timezone before local refs could advance.
- Standardized the displayed author name and kept the upstream license notice unchanged. A byte comparison initially failed because of CRLF/LF; a normalized comparison and git diff confirmed the notice was preserved.
- Fixed the Card Studio color controls: a floated full-width legend required clearing every following sibling, including when the first field was hidden. The fix used `legend~*` and an auto-fit color grid. Verification: 215 pytest and 11 Node tests passed.
- Diagnosed stationary elapsed labels despite a moving progress bar: templates emitted time as text. Added CSS digit reels with millisecond phase and a shared end-of-track deadline. Regression cases covered 59.8s to 1:00, 9:59 to 10:00, and long tracks. Verification: 246 pytest and 11 Node tests passed; independent review found no issues.
- Added five layouts (mini, vinyl, banner, glass, mobile) and ten equalizer styles (dots, vu, ring, ripple, heartbeat, pixel, glow, bubbles, skyline, tunnel). The studio reached 15 themes and 19 equalizers. Verification: 481 pytest and 11 Node tests passed. Review fixed nested SVG namespaces, mobile's empty artwork state, and the picture-disc vinyl design. Layout changes were committed in `385b509`.
- Moved detailed documentation into the GitHub Wiki and then combined it into one top-to-bottom page. The timeline session began from clean master `31bdbc74ab50af9c2928e9c3de32cabd9cb1f530`.

## Environment issues

- On Windows, `api/util` and `api/view.svg.py` are text stubs for Git symlinks. Running the complete suite directly raised `NameError: name 'view' is not defined` from the view.svg stub. Tests must use a disposable snapshot with those targets resolved; preserve the original symlinks in the repository.
- PowerShell's default pipe encoding can turn Vietnamese literals into question marks. Use UTF-8 explicitly when passing scripts. New project text is now required to be English.
- Graph refresh and artifact writes sometimes failed inside the sandbox with `PermissionError` on `graphify-out/.rebuild.lock` or its review directory. The same commands succeeded with the approved outside-sandbox execution. Graph output remains ignored.
- Browser inventory was empty. Tests validate rendering, markup, and timing calculations; they do not prove actual browser clipping, baselines, or animation behavior. Older live Vercel checks also lacked connector project permissions.
- An rg glob embedded in a Windows path produced OS error 123; pass the pattern through `rg -g` instead.

## All-theme timeline fix - 2026-11-12

- The user requested progress bars and elapsed clocks for every unsupported theme. Reproduction showed missing timelines in mini/default/compact/karaoke/natemoo-re/novatorem and static labels in Apple/Spotify Embed. Existing clock tests excluded mini and all classic themes.
- Added failing real-template tests, then reused the shared timeline macros across all 15 themes. Split timeline CSS from Spotify layout CSS so classic layouts retain their styling. Removed fabricated Apple/Embed timestamps and use actual elapsed/total times.
- Mini gained 24px while displaying a timeline; five classic layouts gained 33px. Recent tracks remain at 0:00, offline hides the timeline, missing/invalid duration stays static, and out-of-range progress is clamped.
- Full verification: 706 pytest passed; 11 Node tests passed; 105 SVG previews were valid. Independent review ran 602 view tests and found no issues. AST comparison confirmed only make_svg changed among Python functions; Spotify fetching/cache functions, Firestore, symlink stubs, and license notices were unchanged.
- Preview and verification artifacts are in `graphify-out/timeline-review/`. The graph was refreshed to 545 nodes, 772 edges, and 38 communities. Actual browser rendering remains unverified.
- Published commit `3e5f70d412d121c1edd6c9e2b64a5685d3c51154` and annotated tag V1.0.1 atomically. Existing V1.0.0 still points to `31bdbc7`.
- During publication, release ID 442704488 was externally retagged from V1.0.0 to V1.0.1. Its old title was corrected after checking the release ID and update timestamp. The user subsequently requested English project content; a follow-up documentation correction updates the release and current project additions accordingly.
- Git Credential Manager already had the LienThuan04 account. Credential fill without a username failed in noninteractive mode; explicitly selecting `username=LienThuan04` resolved it. Credentials stayed in process memory and were never printed.
- English release notes were published and the Wiki timeline updates were pushed in `956a583`. The first language scan rejected an English heading's em dash; checking non-ASCII letters instead correctly validated the English additions while permitting punctuation.
- English documentation correction was committed as `ab8350e` and pushed. V1.0.1 was moved with an explicit lease protecting its previous annotated tag object. Final release bookkeeping is recorded separately; resolve the final commit from the tag.
