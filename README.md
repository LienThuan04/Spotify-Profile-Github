# Spotify-Profile-Github

Spotify now playing cards for GitHub profiles, maintained by [LianHarman(LienThuan04)](https://github.com/LienThuan04).

Running on Vercel serverless function, store data in Firebase (store only access_token, refresh_token, token_expired_timestamp)

## Table of Contents

- [Connect And Grant Permission](#connect-and-grant-permission)
- [Themes](#themes)
- [Equalizer styles](#equalizer-styles)
- [Options](#options)
- [Running locally without Vercel](#running-for-development-locally-without-vercel)
- [Running locally with Vercel](#running-for-development-locally-with-vercel)
- [Setting up Vercel](#setting-up-vercel)
- [Setting up Firebase](#setting-up-firebase)
- [Setting up Spotify dev](#setting-up-spotify-dev)
- [Running locally](#running-locally)
- [How to Contribute](#how-to-contribute)
- [Known Bugs](#known-bugs)

## Connect And Grant Permission

- Click `Connect with Spotify` button below to grant permission

[<img src="/img/btn-spotify.png">](https://spotify-github-profile-lian-harman.vercel.app/api/login)

After connecting, **Card Studio** lets you choose a layout, equalizer, colors, corner radius and playback options with a live preview. Copy the result as Markdown, HTML or an image URL; reset settings at any time. Controls adapt to the selected theme.

## Themes

Every preview below uses this project's deployment. Cards show the current track, a randomly selected recently played track when playback stops, or an offline status if no track is available. Connect your Spotify account above to generate a URL with your own `uid`.

<table>
  <tr>
    <td align="center" valign="top" width="50%"><code>theme=spotify-card</code><br/><img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card" width="100%" alt="theme=spotify-card" /></td>
    <td align="center" valign="top" width="50%"><code>theme=spotify-bar</code><br/><img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-bar" width="100%" alt="theme=spotify-bar" /></td>
  </tr>
  <tr>
    <td align="center" valign="top" width="50%"><code>theme=spotify-album</code><br/><img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-album" width="100%" alt="theme=spotify-album" /></td>
    <td align="center" valign="top" width="50%"><code>theme=default</code><br/><img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=default" width="100%" alt="theme=default" /></td>
  </tr>
  <tr>
    <td align="center" valign="top" width="50%"><code>theme=compact</code><br/><img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=compact" width="100%" alt="theme=compact" /></td>
    <td align="center" valign="top" width="50%"><code>theme=natemoo-re</code><br/><img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=natemoo-re" width="100%" alt="theme=natemoo-re" /></td>
  </tr>
  <tr>
    <td align="center" valign="top" width="50%"><code>theme=novatorem</code><br/><img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=novatorem" width="100%" alt="theme=novatorem" /></td>
    <td align="center" valign="top" width="50%"><code>theme=karaoke</code><br/><img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=karaoke" width="100%" alt="theme=karaoke" /></td>
  </tr>
  <tr>
    <td align="center" valign="top" width="50%"><code>theme=apple</code><br/><img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=apple" width="100%" alt="theme=apple" /></td>
    <td align="center" valign="top" width="50%"><code>theme=spotify-embed</code><br/><img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-embed" width="100%" alt="theme=spotify-embed" /></td>
  </tr>
</table>

## Equalizer styles

`eq_style` changes the equalizer on `spotify-card`, `spotify-bar` and `spotify-album`. Animated styles use pure CSS without JavaScript. They animate during playback, pause for recently played tracks, and are hidden offline; `none` always hides the equalizer. `iso`, `ribbon` and `floor` add a 3D depth effect.

<table>
  <tr>
    <td align="center" valign="top" width="50%"><code>eq_style=bars</code><br/><img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=bars" width="100%" alt="theme=spotify-card&eq_style=bars" /></td>
    <td align="center" valign="top" width="50%"><code>eq_style=spectrum</code><br/><img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=spectrum" width="100%" alt="theme=spotify-card&eq_style=spectrum" /></td>
  </tr>
  <tr>
    <td align="center" valign="top" width="50%"><code>eq_style=mirror</code><br/><img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=mirror" width="100%" alt="theme=spotify-card&eq_style=mirror" /></td>
    <td align="center" valign="top" width="50%"><code>eq_style=wave</code><br/><img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=wave" width="100%" alt="theme=spotify-card&eq_style=wave" /></td>
  </tr>
  <tr>
    <td align="center" valign="top" width="50%"><code>eq_style=pulse</code><br/><img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=pulse" width="100%" alt="theme=spotify-card&eq_style=pulse" /></td>
    <td align="center" valign="top" width="50%"><code>eq_style=iso</code><br/><img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=iso" width="100%" alt="theme=spotify-card&eq_style=iso" /></td>
  </tr>
  <tr>
    <td align="center" valign="top" width="50%"><code>eq_style=ribbon</code><br/><img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=ribbon" width="100%" alt="theme=spotify-card&eq_style=ribbon" /></td>
    <td align="center" valign="top" width="50%"><code>eq_style=floor</code><br/><img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=floor" width="100%" alt="theme=spotify-card&eq_style=floor" /></td>
  </tr>
  <tr>
    <td align="center" valign="top" width="50%"><code>eq_style=none</code><br/><img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=none" width="100%" alt="theme=spotify-card&eq_style=none" /></td>
  </tr>
</table>

## Options

Add these as query parameters to your card URL alongside your `uid`. The previews use `theme=spotify-card`, with `spectrum` to show equalizer color changes; the `mode` example uses `theme=apple`.

| Parameter | Description | Default | Live preview |
|-----------|-------------|---------|--------------|
| `theme` | Card layout — see [Themes](#themes). | `default` | <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card" width="260" alt="theme=spotify-card" /> |
| `eq_style` | Equalizer for `spotify-card`, `spotify-bar`, `spotify-album` — see [Equalizer styles](#equalizer-styles). Unknown values fall back to `bars`. | `bars` | <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=iso" width="260" alt="theme=spotify-card&eq_style=iso" /> |
| `background_color` | Background color (hex without `#`). | `121212` | <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;background_color=0d1117" width="260" alt="theme=spotify-card&background_color=0d1117" /> |
| `border_radius` | Border radius in pixels. | `10` | <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;border_radius=24" width="260" alt="theme=spotify-card&border_radius=24" /> |
| `bar_color` | Equalizer color (hex without `#`). | `1ed760` for `spotify-card`, `spotify-bar`, `spotify-album`; `53b14f` otherwise | <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=spectrum&amp;bar_color=ff4fd8" width="260" alt="theme=spotify-card&eq_style=spectrum&bar_color=ff4fd8" /> |
| `bar_color_cover` | Take the equalizer color from the album cover (`true`/`false`). | `false` | <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=spectrum&amp;bar_color_cover=true" width="260" alt="theme=spotify-card&eq_style=spectrum&bar_color_cover=true" /> |
| `cover_image` | Show the album cover (`true`/`false`). | `true` | <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;cover_image=false" width="260" alt="theme=spotify-card&cover_image=false" /> |
| `show_offline` | Show "Not playing" instead of a recently played track when nothing is playing (`true`/`false`). | `false` | <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;show_offline=true" width="260" alt="theme=spotify-card&show_offline=true" /> |
| `interchange` | Swap artist and song name positions (`true`/`false`). | `false` | <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;interchange=true" width="260" alt="theme=spotify-card&interchange=true" /> |
| `mode` | Color mode for `apple` and `spotify-embed` (`light`/`dark`). | `light` | <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=apple&amp;mode=dark" width="260" alt="theme=apple&mode=dark" /> |
| `hide_remaster` | Strip "Remastered" suffixes from song titles (`true`/`false`). | `false` | <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;hide_remaster=true" width="260" alt="theme=spotify-card&hide_remaster=true" /> |
| `profanity` | Censor profanity in titles (`true`/`false`). | `false` | <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;profanity=true" width="260" alt="theme=spotify-card&profanity=true" /> |
| `redirect` | Open the current or recently played track on Spotify instead of returning an image — use it as the link target (`true`/`false`). | `false` | — |

### Example

```
https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=YOUR_UID&theme=spotify-card&eq_style=iso&cover_image=true&show_offline=true
```

Wrap it in a link with `redirect=true` so clicking the card opens the song:

```html
<a href="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=YOUR_UID&amp;redirect=true">
  <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=YOUR_UID&amp;theme=spotify-card&amp;eq_style=iso" alt="Spotify Now Playing" />
</a>
```

## Running for development locally without Vercel

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


## Running for development locally with Vercel

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

## How to Contribute

- Develop locally and submit a pull request!
- Submit newly encountered bugs to the [Issues](https://github.com/LienThuan04/Spotify-Profile-Github/issues) page
- Submit feature suggestions to the [Issues](https://github.com/LienThuan04/Spotify-Profile-Github/issues) page, with the label [Feature Suggestion]

## Known Bugs

[404/500 Error when playing local files](https://github.com/LienThuan04/Spotify-Profile-Github/issues)

## Other Platforms
- [Apple Music GitHub Profile](https://github.com/rayriffy/apple-music-github-profile)
