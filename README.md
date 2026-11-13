# Spotify-Profile-Github

Spotify "now playing" cards for GitHub profiles, maintained by [LianHarman(LienThuan04)](https://github.com/LienThuan04). 15 layouts, 19 animated equalizers, all rendered as plain SVG so they work inside any README.

<p align="center">
  <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=iso" width="49%" alt="theme=spotify-card&amp;eq_style=iso" />
  <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-vinyl" width="49%" alt="theme=spotify-vinyl" />
</p>

<sub>Live cards from the maintainer's account — they show what is playing right now.</sub>

## Quick start

1. Connect your Spotify account:

   [<img src="/img/btn-spotify.png">](https://spotify-github-profile-lian-harman.vercel.app/api/login)

2. **Card Studio** opens. Pick a layout, an equalizer, colors and playback options while watching a live preview.
3. Copy the Markdown or HTML and paste it into your profile `README.md`:

```html
<a href="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=YOUR_UID&amp;redirect=true">
  <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=YOUR_UID&amp;theme=spotify-card&amp;eq_style=bars" alt="Spotify Now Playing" />
</a>
```

## Documentation

Everything else lives on one [wiki page](https://github.com/LienThuan04/Spotify-Profile-Github/wiki) so this page stays short:

| Page | Contents |
|---|---|
| [Card Studio](https://github.com/LienThuan04/Spotify-Profile-Github/wiki#card-studio) | Build your card step by step |
| [Themes](https://github.com/LienThuan04/Spotify-Profile-Github/wiki#themes) | 15 layouts with sizes and live previews |
| [Equalizer styles](https://github.com/LienThuan04/Spotify-Profile-Github/wiki#equalizer-styles) | 19 animations, including 3D styles |
| [Options](https://github.com/LienThuan04/Spotify-Profile-Github/wiki#options) | Every URL parameter with defaults and previews |
| [Development](https://github.com/LienThuan04/Spotify-Profile-Github/wiki#development) | Self-hosting on Vercel, Firebase setup, running tests |

## Feedback and ideas

More themes and features are still in development. Have an idea for a theme or a feature? Send it to me on [my website](https://lianharman.netlify.app) or through [my GitHub profile](https://github.com/LienThuan04). Card Studio links there too: the **Coming soon** tile under the themes and **Suggest a theme or feature** in the footer.

## Contributing

Bugs and ideas go to [Issues](https://github.com/LienThuan04/Spotify-Profile-Github/issues). Development setup is in the [Development wiki page](https://github.com/LienThuan04/Spotify-Profile-Github/wiki#development).

Known bug: local files (not from Spotify's catalogue) can return a 404/500 card.

## License

MIT — see [LICENSE](LICENSE) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
