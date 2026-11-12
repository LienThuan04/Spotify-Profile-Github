# Development

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

## Setting up Vercel

- [Create a new Vercel project by importing](https://vercel.com/import) your project on GitHub

## Setting up Firebase

- Create [a new Firebase project](https://console.firebase.google.com/u/0/)
- Create a new Cloud Firestore in the project
- Download configuration JSON file from _Project settings_ > _Service accounts_ > _Generate new private key_
- Convert private key content as BASE64
  - You can use Encode/Decode extension in VSCode to do so
  - This key will be used in step explained below

## Setting up Spotify dev

- Login to [developer.spotify.com](https://developer.spotify.com/dashboard/applications)
- Create a new project
- Edit settings to add _Redirect URIs_
  - add `http://localhost:3000/api/callback`

## Running locally

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

## Run unittest

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

---

[Home](Home.md) · [Themes](Themes.md) · [Equalizer styles](Equalizer-Styles.md) · [Options](Options.md) · [Card Studio](Card-Studio.md) · [Development](Development.md)
