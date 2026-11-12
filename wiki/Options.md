# Options

Add these as query parameters to your card URL alongside your `uid`. The previews use `theme=spotify-card`, with `spectrum` to show equalizer color changes; the `mode` example uses `theme=apple`.

| Parameter | Description | Default | Live preview |
|-----------|-------------|---------|--------------|
| `theme` | Card layout — see [Themes](Themes.md). | `default` | <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card" width="260" alt="theme=spotify-card" /> |
| `eq_style` | Equalizer for Spotify themes — see [Equalizer styles](Equalizer-Styles.md). Unknown values fall back to `bars`. | `bars` | <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=iso" width="260" alt="theme=spotify-card&eq_style=iso" /> |
| `background_color` | Background color (hex without `#`). | `121212` | <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;background_color=0d1117" width="260" alt="theme=spotify-card&background_color=0d1117" /> |
| `border_radius` | Border radius in pixels. | `10` | <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;border_radius=24" width="260" alt="theme=spotify-card&border_radius=24" /> |
| `bar_color` | Equalizer color (hex without `#`). | `1ed760` for Spotify themes; `53b14f` otherwise | <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=spectrum&amp;bar_color=ff4fd8" width="260" alt="theme=spotify-card&eq_style=spectrum&bar_color=ff4fd8" /> |
| `bar_color_cover` | Take the equalizer color from the album cover (`true`/`false`). | `false` | <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;eq_style=spectrum&amp;bar_color_cover=true" width="260" alt="theme=spotify-card&eq_style=spectrum&bar_color_cover=true" /> |
| `cover_image` | Show the album cover (`true`/`false`). | `true` | <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;cover_image=false" width="260" alt="theme=spotify-card&cover_image=false" /> |
| `show_offline` | Show "Not playing" instead of a recently played track when nothing is playing (`true`/`false`). | `false` | <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;show_offline=true" width="260" alt="theme=spotify-card&show_offline=true" /> |
| `interchange` | Swap artist and song name positions (`true`/`false`). | `false` | <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;interchange=true" width="260" alt="theme=spotify-card&interchange=true" /> |
| `mode` | Color mode for `apple` and `spotify-embed` (`light`/`dark`). | `light` | <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=apple&amp;mode=dark" width="260" alt="theme=apple&mode=dark" /> |
| `hide_remaster` | Strip "Remastered" suffixes from song titles (`true`/`false`). | `false` | <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;hide_remaster=true" width="260" alt="theme=spotify-card&hide_remaster=true" /> |
| `profanity` | Censor profanity in titles (`true`/`false`). | `false` | <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=316jq374l35difgshqzgcymbjolu&amp;theme=spotify-card&amp;profanity=true" width="260" alt="theme=spotify-card&profanity=true" /> |
| `redirect` | Open the current or recently played track on Spotify instead of returning an image — use it as the link target (`true`/`false`). | `false` | — |

## Example

```
https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=YOUR_UID&theme=spotify-card&eq_style=iso&cover_image=true&show_offline=true
```

Wrap it in a link with `redirect=true` so clicking the card opens the song:

```html
<a href="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=YOUR_UID&amp;redirect=true">
  <img src="https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=YOUR_UID&amp;theme=spotify-card&amp;eq_style=iso" alt="Spotify Now Playing" />
</a>
```

---

[Home](Home.md) · [Themes](Themes.md) · [Equalizer styles](Equalizer-Styles.md) · [Options](Options.md) · [Card Studio](Card-Studio.md) · [Development](Development.md)
