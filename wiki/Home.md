<p align="center"><img src="https://github.com/LienThuan04/Spotify-SPARK/raw/master/api/templates/_builder/icon.svg" width="96" alt="Spotify-SPARK icon" /></p>

# Spotify-SPARK Wiki

**SPARK** is the Spotify Presence Activity Render Kit: SVG cards of what is playing on Spotify, for GitHub profiles, by [LianHarman(LienThuan04)](https://github.com/LienThuan04). Everything is on this one page — use the contents to jump around.

**Quick start:** [connect with Spotify](https://spotify-spark.vercel.app/api/login) → build your card in [Card Studio](#card-studio) → paste the code into your profile README.

## Contents

1. [Card Studio](#card-studio)
2. [Themes](#themes)
3. [Equalizer styles](#equalizer-styles)
4. [Options](#options)
5. [Development](#development)
6. [Feedback and ideas](#feedback-and-ideas)

## Card Studio

Card Studio is the page you land on after connecting your Spotify account. It builds your card URL for you, with a live preview.

1. **Connect** — open [https://spotify-spark.vercel.app/api/login](https://spotify-spark.vercel.app/api/login) and allow access to your currently playing and recently played tracks.
2. **Choose a layout** — pick one of the 15 [themes](#themes). Controls that do not apply to the chosen theme are hidden.
3. **Pick an equalizer** — Spotify themes support 19 [equalizer styles](#equalizer-styles).
4. **Tune colors and shape** — background color, equalizer color (or take it from the album cover), corner radius, and appearance (light/dark) for `apple` and `spotify-embed`.
5. **Playback options** — show the album cover, show "Not playing" when idle, swap artist/title, hide "Remastered" suffixes, censor profanity, and make the card open the song on click.
6. **Copy** — choose Markdown, HTML or the plain image URL and paste it into your profile `README.md`. Use **Reset** to start over.
7. **Share ideas** — the **Coming soon** tile after the themes and **Suggest a theme or feature** in the footer open the feedback page (`FEEDBACK_URL`, or the owner's GitHub profile).

Every parameter Card Studio sets is documented in [Options](#options), so you can also edit the URL by hand.

<sub>[↑ Back to contents](#contents)</sub>

## Themes

| Theme | Size | Best for |
|---|---|---|
| `spotify-card` | 400×200 | Default choice; sits next to other 400×200 cards |
| `spotify-bar` | 400×112 | Compact strip under your bio |
| `spotify-album` | 240 wide | Artwork-first column |
| `spotify-mini` | 320×96 (offline: 320×72) | Tiny pill with playback timeline |
| `spotify-vinyl` | 400×200 | Spinning picture disc made from the album cover |
| `spotify-banner` | 800×180 | Full-width hero banner |
| `spotify-glass` | 400×200 | Frosted glass over the blurred cover |
| `spotify-mobile` | 280×500 | Phone "Now Playing" screen |
| `default`, `compact`, `natemoo-re`, `novatorem`, `karaoke`, `apple`, `spotify-embed` | varies | Classic themes kept for existing links |


Every preview below uses this project's deployment. Cards show the current track, a randomly selected recently played track when playback stops, or an offline status if no track is available. Connect your Spotify account above to generate a URL with your own `uid`.

All 15 themes include a progress bar with elapsed time and total duration. During playback, CSS advances the bar and elapsed clock together, stopping at the end of the track. Recently played tracks stay at 0:00; offline cards hide the timeline. If Spotify does not provide timing, the timeline stays static. Pause, seeking and track changes require a fresh image response. Classic layouts grow by 33px to fit the timeline; Apple and Spotify Embed keep their existing size.

<table>
  <tr>
    <td align="center" valign="top" width="50%"><code>theme=spotify-card</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card" width="100%" alt="theme=spotify-card" /></td>
    <td align="center" valign="top" width="50%"><code>theme=spotify-bar</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-bar" width="100%" alt="theme=spotify-bar" /></td>
  </tr>
  <tr>
    <td align="center" valign="top" width="50%"><code>theme=spotify-album</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-album" width="100%" alt="theme=spotify-album" /></td>
    <td align="center" valign="top" width="50%"><code>theme=spotify-mini</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-mini" width="100%" alt="theme=spotify-mini" /></td>
  </tr>
  <tr>
    <td align="center" valign="top" width="50%"><code>theme=spotify-vinyl</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-vinyl" width="100%" alt="theme=spotify-vinyl" /></td>
    <td align="center" valign="top" width="50%"><code>theme=spotify-banner</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-banner" width="100%" alt="theme=spotify-banner" /></td>
  </tr>
  <tr>
    <td align="center" valign="top" width="50%"><code>theme=spotify-glass</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-glass" width="100%" alt="theme=spotify-glass" /></td>
    <td align="center" valign="top" width="50%"><code>theme=spotify-mobile</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-mobile" width="100%" alt="theme=spotify-mobile" /></td>
  </tr>
  <tr>
    <td align="center" valign="top" width="50%"><code>theme=default</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=default" width="100%" alt="theme=default" /></td>
    <td align="center" valign="top" width="50%"><code>theme=compact</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=compact" width="100%" alt="theme=compact" /></td>
  </tr>
  <tr>
    <td align="center" valign="top" width="50%"><code>theme=natemoo-re</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=natemoo-re" width="100%" alt="theme=natemoo-re" /></td>
    <td align="center" valign="top" width="50%"><code>theme=novatorem</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=novatorem" width="100%" alt="theme=novatorem" /></td>
  </tr>
  <tr>
    <td align="center" valign="top" width="50%"><code>theme=karaoke</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=karaoke" width="100%" alt="theme=karaoke" /></td>
    <td align="center" valign="top" width="50%"><code>theme=apple</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=apple" width="100%" alt="theme=apple" /></td>
  </tr>
  <tr>
    <td align="center" valign="top" width="50%"><code>theme=spotify-embed</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-embed" width="100%" alt="theme=spotify-embed" /></td>
    <td align="center" valign="top" width="50%"></td>
  </tr>
</table>

<sub>[↑ Back to contents](#contents)</sub>

## Equalizer styles

Styles at a glance:

- **Classic** — `bars`, `spectrum`, `mirror`, `wave`, `pulse`
- **3D depth** — `iso`, `ribbon`, `floor`, `skyline`, `tunnel`
- **Retro & fun** — `dots`, `vu`, `ring`, `ripple`, `heartbeat`, `pixel`, `glow`, `bubbles`
- **Off** — `none`

Equalizers animate only while a track is playing; recently played cards show them still, and offline cards hide them.


`eq_style` changes the equalizer on `spotify-card`, `spotify-bar`, `spotify-album`, `spotify-mini`, `spotify-vinyl`, `spotify-banner`, `spotify-glass`, and `spotify-mobile`. Animated styles use pure CSS without JavaScript. They animate during playback, pause for recently played tracks, and are hidden offline; `none` always hides the equalizer. `iso`, `ribbon`, `floor`, `skyline`, and `tunnel` add a 3D depth effect.

<table>
  <tr>
    <td align="center" valign="top" width="50%"><code>eq_style=bars</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=bars" width="100%" alt="theme=spotify-card&eq_style=bars" /></td>
    <td align="center" valign="top" width="50%"><code>eq_style=spectrum</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=spectrum" width="100%" alt="theme=spotify-card&eq_style=spectrum" /></td>
  </tr>
  <tr>
    <td align="center" valign="top" width="50%"><code>eq_style=mirror</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=mirror" width="100%" alt="theme=spotify-card&eq_style=mirror" /></td>
    <td align="center" valign="top" width="50%"><code>eq_style=wave</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=wave" width="100%" alt="theme=spotify-card&eq_style=wave" /></td>
  </tr>
  <tr>
    <td align="center" valign="top" width="50%"><code>eq_style=pulse</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=pulse" width="100%" alt="theme=spotify-card&eq_style=pulse" /></td>
    <td align="center" valign="top" width="50%"><code>eq_style=iso</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=iso" width="100%" alt="theme=spotify-card&eq_style=iso" /></td>
  </tr>
  <tr>
    <td align="center" valign="top" width="50%"><code>eq_style=ribbon</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=ribbon" width="100%" alt="theme=spotify-card&eq_style=ribbon" /></td>
    <td align="center" valign="top" width="50%"><code>eq_style=floor</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=floor" width="100%" alt="theme=spotify-card&eq_style=floor" /></td>
  </tr>
  <tr>
    <td align="center" valign="top" width="50%"><code>eq_style=dots</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=dots" width="100%" alt="theme=spotify-card&eq_style=dots" /></td>
    <td align="center" valign="top" width="50%"><code>eq_style=vu</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=vu" width="100%" alt="theme=spotify-card&eq_style=vu" /></td>
  </tr>
  <tr>
    <td align="center" valign="top" width="50%"><code>eq_style=ring</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=ring" width="100%" alt="theme=spotify-card&eq_style=ring" /></td>
    <td align="center" valign="top" width="50%"><code>eq_style=ripple</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=ripple" width="100%" alt="theme=spotify-card&eq_style=ripple" /></td>
  </tr>
  <tr>
    <td align="center" valign="top" width="50%"><code>eq_style=heartbeat</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=heartbeat" width="100%" alt="theme=spotify-card&eq_style=heartbeat" /></td>
    <td align="center" valign="top" width="50%"><code>eq_style=pixel</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=pixel" width="100%" alt="theme=spotify-card&eq_style=pixel" /></td>
  </tr>
  <tr>
    <td align="center" valign="top" width="50%"><code>eq_style=glow</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=glow" width="100%" alt="theme=spotify-card&eq_style=glow" /></td>
    <td align="center" valign="top" width="50%"><code>eq_style=bubbles</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=bubbles" width="100%" alt="theme=spotify-card&eq_style=bubbles" /></td>
  </tr>
  <tr>
    <td align="center" valign="top" width="50%"><code>eq_style=skyline</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=skyline" width="100%" alt="theme=spotify-card&eq_style=skyline" /></td>
    <td align="center" valign="top" width="50%"><code>eq_style=tunnel</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=tunnel" width="100%" alt="theme=spotify-card&eq_style=tunnel" /></td>
  </tr>
  <tr>
    <td align="center" valign="top" width="50%"><code>eq_style=none</code><br/><img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=none" width="100%" alt="theme=spotify-card&eq_style=none" /></td>
    <td align="center" valign="top" width="50%"></td>
  </tr>
</table>

<sub>[↑ Back to contents](#contents)</sub>

## Options

Add these as query parameters to your card URL alongside your `uid`. The previews use `theme=spotify-card`, with `spectrum` to show equalizer color changes; the `mode` example uses `theme=apple`.

| Parameter | Description | Default | Live preview |
|-----------|-------------|---------|--------------|
| `theme` | Card layout — see [Themes](#themes). | `default` | <img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card" width="260" alt="theme=spotify-card" /> |
| `eq_style` | Equalizer for Spotify themes — see [Equalizer styles](#equalizer-styles). Unknown values fall back to `bars`. | `bars` | <img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=iso" width="260" alt="theme=spotify-card&eq_style=iso" /> |
| `background_color` | Background color (hex without `#`). | `121212` | <img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;background_color=0d1117" width="260" alt="theme=spotify-card&background_color=0d1117" /> |
| `border_radius` | Border radius in pixels. | `10` | <img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;border_radius=24" width="260" alt="theme=spotify-card&border_radius=24" /> |
| `bar_color` | Equalizer color (hex without `#`). | `1ed760` for Spotify themes; `53b14f` otherwise | <img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=spectrum&amp;bar_color=ff4fd8" width="260" alt="theme=spotify-card&eq_style=spectrum&bar_color=ff4fd8" /> |
| `bar_color_cover` | Take the equalizer color from the album cover (`true`/`false`). | `false` | <img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=spectrum&amp;bar_color_cover=true" width="260" alt="theme=spotify-card&eq_style=spectrum&bar_color_cover=true" /> |
| `cover_image` | Show the album cover (`true`/`false`). | `true` | <img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;cover_image=false" width="260" alt="theme=spotify-card&cover_image=false" /> |
| `show_offline` | Show "Not playing" instead of a recently played track when nothing is playing (`true`/`false`). | `false` | <img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;show_offline=true" width="260" alt="theme=spotify-card&show_offline=true" /> |
| `interchange` | Swap artist and song name positions (`true`/`false`). | `false` | <img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;interchange=true" width="260" alt="theme=spotify-card&interchange=true" /> |
| `mode` | Color mode for `apple` and `spotify-embed` (`light`/`dark`). | `light` | <img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=apple&amp;mode=dark" width="260" alt="theme=apple&mode=dark" /> |
| `hide_remaster` | Strip "Remastered" suffixes from song titles (`true`/`false`). | `false` | <img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;hide_remaster=true" width="260" alt="theme=spotify-card&hide_remaster=true" /> |
| `profanity` | Censor profanity in titles (`true`/`false`). | `false` | <img src="https://spotify-spark.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;profanity=true" width="260" alt="theme=spotify-card&profanity=true" /> |
| `redirect` | Open the current or recently played track on Spotify instead of returning an image — use it as the link target (`true`/`false`). | `false` | — |

### Example

```
https://spotify-spark.vercel.app/api/view?uid=YOUR_UID&theme=spotify-card&eq_style=iso&cover_image=true&show_offline=true
```

Wrap it in a link with `redirect=true` so clicking the card opens the song:

```html
<a href="https://spotify-spark.vercel.app/api/view?uid=YOUR_UID&amp;redirect=true">
  <img src="https://spotify-spark.vercel.app/api/view?uid=YOUR_UID&amp;theme=spotify-card&amp;eq_style=iso" alt="Spotify Now Playing" />
</a>
```

<sub>[↑ Back to contents](#contents)</sub>

## Development

### Running for development locally without Vercel

To run the application locally without Vercel:

1. Copy `.env.example` to `.env` in the root directory and replace the placeholder values with your actual configuration.

2. Install the required dependencies:
   ```sh
   pip install -r api/requirements.txt
   ```

3. Run the application:
   ```sh
   python api/app.py
   ```

4. Access the login page at http://localhost:3000/api/login

Note: Ensure your Spotify app's redirect URI is set to `http://localhost:3000/api/callback` and `BASE_URL` in `.env` is set to `http://localhost:3000/api`.


### Running for development locally with Vercel

To develop locally, you need:

- A copy of this project in your GitHub repository
- A Vercel project connected with your repository
- A Firebase project with Cloud Firestore setup
- A Spotify developer account

### Setting up Vercel

- [Create a new Vercel project by importing](https://vercel.com/import) your project on GitHub

### Setting up Firebase

- Create [a new Firebase project](https://console.firebase.google.com/u/0/)
- Create a new Cloud Firestore in the project
- Download configuration JSON file from _Project settings_ > _Service accounts_ > _Generate new private key_
- Convert private key content as BASE64
  - You can use Encode/Decode extension in VSCode to do so
  - This key will be used in step explained below

### Setting up Spotify dev

- Login to [developer.spotify.com](https://developer.spotify.com/dashboard/applications)
- Create a new project
- Edit settings to add _Redirect URIs_
  - add `http://localhost:3000/api/callback`

### Running locally

- Install [Vercel command line](https://vercel.com/download) with `npm i -g vercel`
- Create `.env` file at the root of the project 
- Paste your keys in `SPOTIFY_CLIENT_ID`, `SPOTIFY_SECRET_ID`, and insert the name of your downloaded JSON file in `FIREBASE`


```sh
BASE_URL='http://localhost:3000/api'
SPOTIFY_CLIENT_ID='____'
SPOTIFY_SECRET_ID='____'
FIREBASE='__BASE64_FIREBASE_JSON_FILE__'
```

- Run `vercel dev`

```sh
$ vercel dev
Vercel CLI 20.1.2 dev (beta) — https://vercel.com/feedback
> Ready! Available at http://localhost:3000
```

- Now try to access http://localhost:3000/api/login

### Run unittest

- Test the card builder's URL generation and controls (Node.js 22+):
```sh
node --test tests/test_builder.js
```

- Run all tests
```sh
pytest tests/ -v
```

- Run tests with coverage
```sh
pytest tests/ --cov=api --cov-report=html
```

- Run specific test file
```sh
pytest tests/test_api_view.py -v
```

- Run with maxfail (like CI)
```sh
pytest tests/ --maxfail=5 --disable-warnings -v
```

### How to Contribute

- Develop locally and submit a pull request!
- Submit newly encountered bugs to the [Issues](https://github.com/LienThuan04/Spotify-SPARK/issues) page
- Submit feature suggestions to the [Issues](https://github.com/LienThuan04/Spotify-SPARK/issues) page, with the label [Feature Suggestion]

### Known Bugs

[404/500 Error when playing local files](https://github.com/LienThuan04/Spotify-SPARK/issues)

### Other Platforms
- [Apple Music GitHub Profile](https://github.com/rayriffy/apple-music-github-profile)

<sub>[↑ Back to contents](#contents)</sub>

## Feedback and ideas

More themes and features are still in development. Have an idea for a theme or a feature? Send it to me on [my website](https://lianharman.netlify.app) or through [my GitHub profile](https://github.com/LienThuan04). Card Studio links there too: the **Coming soon** tile under the themes and **Suggest a theme or feature** in the footer.

<sub>[↑ Back to contents](#contents)</sub>
