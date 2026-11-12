# Spotify-Profile-Github

Spotify now playing cards for GitHub profiles, maintained by [Lian Harman (LienThuan04)](https://github.com/LienThuan04).

Running on Vercel serverless function, store data in Firebase (store only access_token, refresh_token, token_expired_timestamp)

## Table of Contents
[Connect And Grant Permission](#connect-and-grant-permission)
[Example](#example)
[Customization](#customization)
[Running for development locally](#running-for-development-locally)
[Setting up Vercel](#setting-up-vercel)
[Setting up Firebase](#setting-up-firebase)
[Setting up Spotify dev](#setting-up-spotify-dev)
[Running locally](#running-locally)
[How to Contribute](#how-to-contribute)
[Known Bugs](#known-bugs)

## Connect And Grant Permission

- Click `Connect with Spotify` button below to grant permission

[<img src="/img/btn-spotify.png">](https://spotify-github-profile-lian-harman.vercel.app/api/login)

## Example

- Default theme

![Spotify-Profile-Github](/img/default.svg)

- Compact theme

![Spotify-Profile-Github](/img/compact.svg)

- Natemoo-re theme

![Spotify-Profile-Github](/img/natemoo-re.svg)

- Novatorem theme

![Spotify-Profile-Github](/img/novatorem.svg)

- Karaoke theme

![Spotify-Profile-Github](/img/karaoke.svg)

- Spotify Embed theme (NEW!)

![Spotify-Profile-Github](/img/spotify-embed.svg)

- Spotify Card — 400×200

![Spotify Card by Lian Harman](/img/spotify-card.svg)

- Spotify Bar — 400×112

![Spotify Bar by Lian Harman](/img/spotify-bar.svg)

- Spotify Album — 240px wide, height adapts to the cover and playback state

![Spotify Album by Lian Harman](/img/spotify-album.svg)

Regenerate these three examples with `python scripts/generate_spotify_examples.py`.

## Customization

You can customize the appearance by adding query parameters to your URL:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `theme` | Theme to use (`default`, `compact`, `natemoo-re`, `novatorem`, `karaoke`, `spotify-embed`, `apple`, `spotify-card`, `spotify-bar`, `spotify-album`) | `default` |
| `background_color` | Background color (hex without #) | `121212` |
| `border_radius` | Border radius in pixels | `10` |
| `bar_color` | Equalizer bar color (hex without #) | `1ed760` for `spotify-card`, `spotify-bar`, `spotify-album`; `53b14f` otherwise |
| `eq_style` | Equalizer for `spotify-card`, `spotify-bar`, `spotify-album`: `bars`, `spectrum`, `mirror`, `wave`, `pulse`, `none`. Unknown values fall back to `bars`. | `bars` |
| `bar_color_cover` | Extract bar color from album cover (`true`/`false`) | `false` |
| `cover_image` | Show album cover image (`true`/`false`) | `true` |
| `show_offline` | Show offline status when not playing (`true`/`false`) | `false` |
| `interchange` | Swap artist and song name positions (`true`/`false`) | `false` |
| `mode` | Color mode for supported themes (`light`/`dark`) | `light` |

### Example

```
https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=YOUR_UID&cover_image=true&theme=default&border_radius=15&bar_color=53b14f
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
