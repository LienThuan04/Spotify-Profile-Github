import pytest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the parent directory to the path to import the api module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


@pytest.fixture
def client():
    """Create a test client for the view Flask application."""
    from api.view import app
    app.config.update({"TESTING": True})
    
    with app.test_client() as client:
        yield client


def test_catch_all_without_uid(client):
    """Test that request without uid parameter returns error."""
    response = client.get('/')
    
    assert response.status_code == 200
    assert response.data == b'not ok'


@patch('api.view.get_song_info')
@patch('api.view.make_svg')
def test_catch_all_with_valid_uid_offline(mock_make_svg, mock_get_song_info, client):
    """Test request with valid uid but user is offline."""
    # Mock song info to return None (offline)
    mock_get_song_info.return_value = (None, False, None, None)
    mock_make_svg.return_value = '<svg>offline</svg>'
    
    response = client.get('/?uid=test_user&show_offline=true')
    
    assert response.status_code == 200
    assert response.mimetype == 'image/svg+xml'
    assert response.headers['Cache-Control'] == 'public, max-age=0, s-maxage=10, stale-while-revalidate=86400'
    
    # Verify make_svg was called with offline parameters
    mock_make_svg.assert_called_once()
    args, kwargs = mock_make_svg.call_args
    assert args[0] in ["Currently not playing on Spotify", "Offline"]  # artist_name
    assert args[1] in ["Offline", "Currently not playing on Spotify"]  # song_name


@patch('api.view.get_song_info')
@patch('api.view.make_svg')
def test_catch_all_with_valid_uid_now_playing(mock_make_svg, mock_get_song_info, client):
    """Test request with valid uid and user is currently playing."""
    # Mock song info for currently playing track
    mock_item = {
        "name": "Test Song",
        "artists": [{"name": "Test Artist"}],
        "album": {"images": [{"url": "http://example.com/image.jpg"}] * 3},
        "uri": "spotify:track:123",
        "currently_playing_type": "track",
        "duration_ms": 240000
    }
    mock_get_song_info.return_value = (mock_item, True, 120000, 240000)
    mock_make_svg.return_value = '<svg>now playing</svg>'
    
    with patch('api.view.load_image', return_value=b'fake_image_data'):
        response = client.get('/?uid=test_user')
        
        assert response.status_code == 200
        assert response.mimetype == 'image/svg+xml'
        assert response.headers['Cache-Control'] == 'public, max-age=0, s-maxage=10, stale-while-revalidate=86400'
        
        # Verify make_svg was called with correct parameters
        mock_make_svg.assert_called_once()
        args, kwargs = mock_make_svg.call_args
        assert args[0] == "Test Artist"  # artist_name
        assert args[1] == "Test Song"    # song_name


@patch('api.view.get_song_info')
def test_catch_all_with_redirect(mock_get_song_info, client):
    """Test request with redirect parameter."""
    mock_item = {
        "uri": "spotify:track:123",
        "currently_playing_type": "track"
    }
    mock_get_song_info.return_value = (mock_item, True, None, None)
    
    response = client.get('/?uid=test_user&redirect=true')
    
    assert response.status_code == 302
    assert response.headers['Location'] == 'spotify:track:123'


@patch('api.view.get_song_info')
def test_catch_all_invalid_token_error(mock_get_song_info, client):
    """Test handling of invalid Spotify token."""
    from util.spotify import InvalidTokenError
    mock_get_song_info.side_effect = InvalidTokenError("Invalid token")
    
    response = client.get('/?uid=test_user')
    
    assert response.status_code == 200
    assert b'Invalid Spotify access_token or refresh_token' in response.data


@pytest.mark.parametrize("theme,expected_height", [
    ("default", 445),
    ("compact", 400),
    ("natemoo-re", 84),
    ("novatorem", 100),
    ("apple", 534),
    ("spotify-embed", 152)
])
@patch('api.view.get_song_info')
@patch('api.view.make_svg')
def test_different_themes(mock_make_svg, mock_get_song_info, client, theme, expected_height):
    """Test different theme parameters."""
    mock_item = {
        "name": "Test Song",
        "artists": [{"name": "Test Artist"}],
        "album": {"images": [{"url": "http://example.com/image.jpg"}] * 3},
        "currently_playing_type": "track"
    }
    mock_get_song_info.return_value = (mock_item, True, None, None)
    mock_make_svg.return_value = f'<svg height="{expected_height}"></svg>'
    
    with patch('api.view.load_image', return_value=b'fake_image_data'):
        response = client.get(f'/?uid=test_user&theme={theme}')
        
        assert response.status_code == 200
        mock_make_svg.assert_called_once()


@pytest.mark.parametrize("cover_image,expected_call", [
    ("true", True),
    ("false", False),
    ("", True)  # default value
])
@patch('api.view.get_song_info')
@patch('api.view.make_svg')
@patch('api.view.load_image')
def test_cover_image_parameter(mock_load_image, mock_make_svg, mock_get_song_info, client, cover_image, expected_call):
    """Test cover_image parameter handling."""
    mock_item = {
        "name": "Test Song", 
        "artists": [{"name": "Test Artist"}],
        "album": {"images": [{"url": "http://example.com/image.jpg"}] * 3},
        "currently_playing_type": "track"
    }
    mock_get_song_info.return_value = (mock_item, False, None, None)
    mock_make_svg.return_value = '<svg></svg>'
    mock_load_image.return_value = b'fake_image_data'
    
    if cover_image:
        response = client.get(f'/?uid=test_user&cover_image={cover_image}')
    else:
        response = client.get('/?uid=test_user')
    
    assert response.status_code == 200
    
    if expected_call:
        mock_load_image.assert_called_once()
    else:
        mock_load_image.assert_not_called()


@patch('api.view.get_song_info')
@patch('api.view.make_svg')
@patch('api.view.load_image')
def test_interchange_parameter(mock_load_image, mock_make_svg, mock_get_song_info, client):
    """Test interchange parameter swaps artist and song names."""
    mock_item = {
        "name": "Test Song",
        "artists": [{"name": "Test Artist"}],
        "album": {"images": [{"url": "http://example.com/image.jpg"}] * 3},
        "currently_playing_type": "track"
    }
    mock_get_song_info.return_value = (mock_item, True, None, None)
    mock_make_svg.return_value = '<svg></svg>'
    mock_load_image.return_value = b'fake_image_data'
    
    response = client.get('/?uid=test_user&interchange=true&cover_image=false')
    
    assert response.status_code == 200
    
    # Verify that artist and song names are swapped
    mock_make_svg.assert_called_once()
    args, kwargs = mock_make_svg.call_args
    assert args[0] == "Test Song"    # artist_name (swapped)
    assert args[1] == "Test Artist"  # song_name (swapped)


def test_helper_function_format_time_ms():
    """Test format_time_ms utility function."""
    from api.view import format_time_ms
    
    assert format_time_ms(0) == "0:00"
    assert format_time_ms(30000) == "0:30"
    assert format_time_ms(90000) == "1:30"
    assert format_time_ms(3600000) == "60:00"
    assert format_time_ms(None) == "0:00"
    assert format_time_ms(-1000) == "0:00"


def test_helper_function_calculate_progress_data():
    """Test calculate_progress_data utility function."""
    from api.view import calculate_progress_data
    
    # Test normal case
    result = calculate_progress_data(60000, 180000)
    assert result["progress_percentage"] == pytest.approx(33.33, rel=1e-2)
    assert result["current_time"] == "1:00"
    assert result["remaining_time"] == "-2:00"
    
    # Test edge cases
    result = calculate_progress_data(None, 180000)
    assert result["progress_percentage"] == 0
    assert result["current_time"] == "0:00"
    
    result = calculate_progress_data(60000, None)
    assert result["progress_percentage"] == 0
    
    # Test progress exceeds duration
    result = calculate_progress_data(200000, 180000)
    assert result["progress_percentage"] == 100


def test_helper_function_isLightOrDark():
    """Test isLightOrDark utility function."""
    from api.view import isLightOrDark
    
    # Test light colors
    assert isLightOrDark([255, 255, 255]) == "light"  # white
    assert isLightOrDark([200, 200, 200]) == "light"  # light gray
    
    # Test dark colors  
    assert isLightOrDark([0, 0, 0]) == "dark"      # black
    assert isLightOrDark([50, 50, 50]) == "dark"   # dark gray


def test_helper_function_encode_html_entities():
    """Test encode_html_entities utility function."""
    from api.view import encode_html_entities
    
    assert encode_html_entities("normal text") == "normal text"
    assert encode_html_entities("text & more") == "text &amp; more"
    assert encode_html_entities("<script>") == "&lt;script&gt;"
    assert encode_html_entities('"quotes"') == "&quot;quotes&quot;"


@patch('api.view.get_song_info')
@patch('api.view.make_svg')
def test_episode_handling(mock_make_svg, mock_get_song_info, client):
    """Test handling of podcast episodes."""
    mock_item = {
        "name": "Test Episode",
        "show": {"publisher": "Test Podcast"},
        "images": [{"url": "http://example.com/image.jpg"}] * 3,
        "currently_playing_type": "episode"
    }
    mock_get_song_info.return_value = (mock_item, True, None, None)
    mock_make_svg.return_value = '<svg></svg>'
    
    with patch('api.view.load_image', return_value=b'fake_image_data'):
        response = client.get('/?uid=test_user')
        
        assert response.status_code == 200
        
        # Verify correct artist/song names for episodes
        mock_make_svg.assert_called_once()
        args, kwargs = mock_make_svg.call_args
        assert args[0] == "Test Podcast"  # artist_name (publisher)
        assert args[1] == "Test Episode"  # song_name


@pytest.mark.parametrize("show_offline,interchange,expected_artist,expected_song", [
    (True, False, "Offline", "Currently not playing on Spotify"),
    (True, True, "Currently not playing on Spotify", "Offline"),
    (False, False, "Offline", "Currently not playing on Spotify"),
    (False, True, "Currently not playing on Spotify", "Offline")
])
@patch('api.view.get_song_info')
@patch('api.view.make_svg')
def test_offline_text_with_interchange(mock_make_svg, mock_get_song_info, client, show_offline, interchange, expected_artist, expected_song):
    """Test offline text with different interchange settings."""
    mock_get_song_info.return_value = (None, False, None, None)
    mock_make_svg.return_value = '<svg></svg>'
    
    params = f'uid=test_user&show_offline={str(show_offline).lower()}&interchange={str(interchange).lower()}'
    response = client.get(f'/?{params}')
    
    assert response.status_code == 200
    
    mock_make_svg.assert_called_once()
    args, kwargs = mock_make_svg.call_args
    assert args[0] == expected_artist  # artist_name
    assert args[1] == expected_song    # song_name


def test_cache_functionality():
    """Test token caching functionality."""
    from api.view import get_cache_token_info, delete_cache_token_info, CACHE_TOKEN_INFO
    
    # Clear cache
    CACHE_TOKEN_INFO.clear()
    
    # Test empty cache
    result = get_cache_token_info("test_uid")
    assert result is None
    
    # Test cache deletion
    CACHE_TOKEN_INFO["test_uid"] = {"access_token": "test_token"}
    delete_cache_token_info("test_uid")
    assert "test_uid" not in CACHE_TOKEN_INFO


@patch('api.view.load_image')
def test_load_image_error_handling(mock_load_image):
    """Test load_image error handling."""
    from api.view import to_img_b64
    
    # Test when load_image returns None
    mock_load_image.return_value = None
    
    # to_img_b64 should handle None gracefully
    result = to_img_b64(None)
    assert result == ""  # Should return empty string for None input


@pytest.mark.parametrize("bar_color,background_color,mode", [
    ("ff0000", "000000", "light"),
    ("00ff00", "ffffff", "dark"), 
    ("0000ff", "121212", "light"),
    ("", "", "")  # test default values
])
@patch('api.view.get_song_info')
@patch('api.view.make_svg')
@patch('api.view.load_image')
def test_color_parameters(mock_load_image, mock_make_svg, mock_get_song_info, client, bar_color, background_color, mode):
    """Test color and mode parameters."""
    mock_item = {
        "name": "Test Song",
        "artists": [{"name": "Test Artist"}],
        "album": {"images": [{"url": "http://example.com/image.jpg"}] * 3},
        "currently_playing_type": "track"
    }
    mock_get_song_info.return_value = (mock_item, True, None, None)
    mock_make_svg.return_value = '<svg></svg>'
    mock_load_image.return_value = b'fake_image_data'
    
    params = f'uid=test_user&bar_color={bar_color}&background_color={background_color}&mode={mode}&cover_image=false'
    response = client.get(f'/?{params}')
    
    assert response.status_code == 200
    mock_make_svg.assert_called_once()


@patch('api.view.get_song_info')
@patch('api.view.make_svg')
@patch('api.view.load_image')
@patch('PIL.Image.open')
@patch('api.view.colorgram.extract')
def test_bar_color_from_cover(mock_extract, mock_pil_open, mock_load_image, mock_make_svg, mock_get_song_info, client):
    """Test extracting bar color from cover image."""
    # Mock PIL Image
    mock_image = MagicMock()
    mock_pil_open.return_value = mock_image
    
    # Mock colorgram color extraction
    mock_color = MagicMock()
    mock_color.rgb.r = 255
    mock_color.rgb.g = 100
    mock_color.rgb.b = 100
    mock_extract.return_value = [mock_color]
    
    mock_item = {
        "name": "Test Song",
        "artists": [{"name": "Test Artist"}],
        "album": {"images": [{"url": "http://example.com/image.jpg"}] * 3},
        "currently_playing_type": "track"
    }
    mock_get_song_info.return_value = (mock_item, True, None, None)
    mock_make_svg.return_value = '<svg></svg>'
    mock_load_image.return_value = b'fake_image_data'
    
    response = client.get('/?uid=test_user&bar_color_cover=true')
    
    assert response.status_code == 200
    mock_extract.assert_called_once()
    mock_make_svg.assert_called_once()


def test_generate_css_bar():
    """Test generate_css_bar utility function."""
    from api.view import generate_css_bar
    
    # Test basic functionality
    css = generate_css_bar(5)
    assert isinstance(css, str)
    assert 'bar:nth-child(' in css
    assert 'animation-duration:' in css
    
    # Test with different number of bars
    css_10 = generate_css_bar(10)
    css_20 = generate_css_bar(20)
    assert len(css_20) > len(css_10)  # More bars should generate more CSS


SPOTIFY_THEMES = [
    "spotify-card", "spotify-bar", "spotify-album",
    "spotify-mini", "spotify-vinyl", "spotify-banner", "spotify-glass", "spotify-mobile",
]
LEGACY_THEMES = ["default", "compact", "karaoke", "natemoo-re", "novatorem", "apple", "spotify-embed"]
TIMELINE_THEMES = [*SPOTIFY_THEMES, *LEGACY_THEMES]
XHTML = "{http://www.w3.org/1999/xhtml}"


@pytest.fixture
def render_spotify():
    from api.view import app, make_svg
    from xml.etree import ElementTree

    def render(**overrides):
        params = dict(
            artist_name="Lazer Boomerang", song_name="Time To Pretend", img="sample",
            is_now_playing=True, cover_image=True, theme="spotify-card",
            bar_color="1ed760", show_offline=False, background_color="121212",
            mode="light", progress_ms=196000, duration_ms=314000,
        )
        params.update(overrides)
        with app.app_context():
            svg = make_svg(**params)
        return ElementTree.fromstring(svg), svg

    return render


@pytest.mark.parametrize("theme,cover,width,height", [
    ("spotify-card", True, "400", "200"),
    ("spotify-card", False, "400", "200"),
    ("spotify-bar", True, "400", "112"),
    ("spotify-bar", False, "400", "112"),
    ("spotify-album", True, "240", "350"),
    ("spotify-album", False, "240", "128"),
])
def test_spotify_dimensions_and_cover(render_spotify, theme, cover, width, height):
    root, _ = render_spotify(theme=theme, cover_image=cover)
    assert (root.get("width"), root.get("height")) == (width, height)
    assert (root.find(f".//{XHTML}img") is not None) == cover
    foreign = root.find("{http://www.w3.org/2000/svg}foreignObject")
    assert foreign.get("height") == height


@pytest.mark.parametrize("theme,cover,width,height", [
    ("spotify-mini", True, "320", "96"),
    ("spotify-mini", False, "320", "96"),
    ("spotify-vinyl", True, "400", "200"),
    ("spotify-vinyl", False, "400", "200"),
    ("spotify-banner", True, "800", "180"),
    ("spotify-banner", False, "800", "180"),
    ("spotify-glass", True, "400", "200"),
    ("spotify-glass", False, "400", "200"),
    ("spotify-mobile", True, "280", "500"),
    ("spotify-mobile", False, "280", "500"),
])
def test_spotify_new_layouts_dimensions(render_spotify, theme, cover, width, height):
    root, svg = render_spotify(theme=theme, cover_image=cover)
    assert (root.get("width"), root.get("height")) == (width, height)
    foreign = root.find("{http://www.w3.org/2000/svg}foreignObject")
    assert foreign.get("height") == height
    if theme in ["spotify-banner", "spotify-glass", "spotify-vinyl"]:
        assert ("--cover: url('data:image/png;base64,sample')" in svg) == cover
    else:
        assert (root.find(f".//{XHTML}img") is not None) == cover


@pytest.mark.parametrize("theme", SPOTIFY_THEMES)
@pytest.mark.parametrize("style,count", [
    ("bars", 4), ("spectrum", 40), ("mirror", 28), ("wave", 0),
    ("pulse", 3), ("iso", 7), ("ribbon", 0), ("floor", 0),
    ("dots", 7), ("vu", 10), ("ring", 0), ("ripple", 0), ("heartbeat", 0),
    ("pixel", 5), ("glow", 4), ("bubbles", 5), ("skyline", 7), ("tunnel", 0),
    ("none", 0), ("invalid", 4),
])
def test_spotify_equalizer_render(render_spotify, theme, style, count):
    root, svg = render_spotify(theme=theme, eq_style=style)
    expected = "bars" if style == "invalid" else style
    equalizers = root.findall(f".//{XHTML}span")
    equalizers = [node for node in equalizers if node.get("class", "").startswith("eq ")]
    if style == "none":
        assert equalizers == []
    else:
        assert len(equalizers) == 1
        eq = equalizers[0]
        assert eq.get("class") == f"eq eq-{expected}"
        assert len(eq.findall(f"{XHTML}i")) == count
        if style == "wave":
            assert len(eq.findall(".//{http://www.w3.org/2000/svg}path")) == 2
        if style in ["spectrum", "mirror"]:
            import re
            for bar in eq:
                duration = int(re.search(r"animation-duration: (\d+)ms", bar.get("style")).group(1))
                assert (350 <= duration <= 800) if style == "spectrum" else (500 <= duration <= 1000)
    assert "<script" not in svg.lower()
    assert 'href="{}"' not in svg


@pytest.mark.parametrize("theme", SPOTIFY_THEMES)
@pytest.mark.parametrize("playing,offline,label,current,animated", [
    (True, False, "NOW PLAYING", "3:16", True),
    (False, False, "RECENTLY PLAYED", "0:00", False),
    (False, True, "NOT PLAYING", None, False),
])
def test_spotify_playback_states(render_spotify, theme, playing, offline, label, current, animated):
    root, svg = render_spotify(theme=theme, is_now_playing=playing, show_offline=offline)
    assert label in "".join(root.itertext())
    progress = root.find(f'.//{XHTML}div[@class="track"]')
    eq = root.find(f'.//{XHTML}span[@class="eq eq-bars"]')
    assert (progress is None) == offline
    assert ("animation: progress 118.0s linear forwards" in svg) == animated
    assert (eq is None) == offline
    if not offline:
        times = root.findall(f'.//{XHTML}div[@class="times"]') + root.findall(f'.//{XHTML}span[@class="times"]')
        time_text = " ".join(" ".join(node.itertext()) for node in times)
        assert current in time_text and "5:14" in time_text
        if not playing:
            assert "width: 0%;" in svg
        if not playing:
            assert ".eq i, .eq svg { animation: none; }" in svg
            assert ".eq b, .eq div, .eq circle, .eq rect, .eq path, .eq line, .eq g { animation: none !important; }" in svg
            if theme == "spotify-vinyl":
                # the record spins only while a track is playing
                assert ".disc { animation: none !important; }" in svg


@pytest.mark.parametrize("progress,duration,width,seconds,total", [
    (0, 240000, "0", "240.0", "4:00"),
    (120000, 240000, "50.0", "120.0", "4:00"),
    (300000, 240000, "100.0", None, "4:00"),
    (None, None, "0", None, "0:00"),
    (0, 0, "0", None, "0:00"),
])
def test_spotify_progress_boundaries(render_spotify, progress, duration, width, seconds, total):
    _, svg = render_spotify(progress_ms=progress, duration_ms=duration)
    assert f"width: {width}%;" in svg
    assert f"<span>{total}</span>" in svg
    if seconds is None:
        assert "animation: progress " not in svg
    else:
        assert f"animation: progress {seconds}s linear forwards" in svg


def _clock_label_at(root, elapsed_seconds):
    """Evaluate the emitted CSS steps timeline; this does not render a browser."""
    import math
    import re

    def declarations(node):
        return dict(part.strip().split(":", 1) for part in node.get("style", "").split(";") if ":" in part)

    clock = root.find(f'.//{XHTML}span[@class="clock"]')
    assert clock is not None, "Playing card must include an animated elapsed clock"
    clock_style = declarations(clock)
    stop_at = float(clock_style["--clock-remaining"].strip().removesuffix("s"))
    if elapsed_seconds >= stop_at:
        return clock.find(f'{XHTML}span[@class="clock-final"]').text
    digits = []
    for reel in clock.findall(f'.//{XHTML}span[@class="clock-reel"]'):
        style = declarations(reel)
        period = float(style["animation-duration"].strip().removesuffix("s"))
        delay = float(style["animation-delay"].strip().removesuffix("s"))
        steps = int(re.fullmatch(r"\s*steps\((\d+),\s*end\)\s*", style["animation-timing-function"]).group(1))
        phase = ((elapsed_seconds - delay) % period) / period
        row = math.floor(phase * steps + 1e-9)
        digits.append(list(reel)[row].text)
    return digits[0] + ":" + "".join(digits[1:])


@pytest.mark.parametrize("theme", TIMELINE_THEMES)
@pytest.mark.parametrize("progress,duration,samples", [
    (196000, 314000, [(0, "3:16"), (1, "3:17"), (4, "3:20"), (118, "5:14"), (160, "5:14")]),
    (59800, 62000, [(0, "0:59"), (.19, "0:59"), (.2, "1:00"), (1.2, "1:01"), (2.2, "1:02"), (8, "1:02")]),
    (599000, 601000, [(0, "9:59"), (.99, "9:59"), (1, "10:00"), (2, "10:01"), (10, "10:01")]),
    (0, 2500, [(0, "0:00"), (.99, "0:00"), (1, "0:01"), (2.49, "0:02"), (2.5, "0:02")]),
])
def test_spotify_elapsed_clock_ticks_and_stops(render_spotify, theme, progress, duration, samples):
    root, svg = render_spotify(theme=theme, progress_ms=progress, duration_ms=duration)
    for elapsed, expected in samples:
        assert _clock_label_at(root, elapsed) == expected
    clock = root.find(f'.//{XHTML}span[@class="clock"]')
    remaining = float(dict(part.strip().split(":", 1) for part in clock.get("style").split(";") if ":" in part)["--clock-remaining"].removesuffix("s"))
    assert remaining == (duration - progress) / 1000
    assert f"animation: progress {remaining}s linear forwards" in svg
    assert "<script" not in svg.lower()


@pytest.mark.parametrize("theme", TIMELINE_THEMES)
@pytest.mark.parametrize("overrides", [
    {"is_now_playing": False},
    {"is_now_playing": False, "show_offline": True},
    {"progress_ms": None},
    {"duration_ms": None},
    {"duration_ms": 0},
    {"progress_ms": 400000, "duration_ms": 314000},
])
def test_spotify_elapsed_clock_requires_active_known_progress(render_spotify, theme, overrides):
    root, svg = render_spotify(theme=theme, **overrides)
    assert root.find(f'.//{XHTML}span[@class="clock"]') is None
    assert "animation: progress " not in svg


@pytest.mark.parametrize("theme", TIMELINE_THEMES)
@pytest.mark.parametrize("overrides,current,total,width,animated", [
    ({}, "3:16", "5:14", "62.42038216560509", True),
    ({"is_now_playing": False}, "0:00", "5:14", "0", False),
    ({"progress_ms": None}, "0:00", "5:14", "0", False),
    ({"duration_ms": None}, "0:00", "0:00", "0", False),
    ({"duration_ms": 0}, "0:00", "0:00", "0", False),
    ({"duration_ms": -1000}, "0:00", "0:00", "0", False),
    ({"progress_ms": -500}, "0:00", "5:14", "0", True),
    ({"progress_ms": 400000}, "5:14", "5:14", "100.0", False),
])
def test_all_theme_timelines_use_real_playback(render_spotify, theme, overrides, current, total, width, animated):
    root, svg = render_spotify(theme=theme, **overrides)
    progress = root.find(f'.//{XHTML}div[@class="progress"]')
    if progress is None:
        progress = root.find(f'.//{XHTML}div[@class="progress progress-inline"]')
    assert progress is not None, f"{theme} must show a playback timeline"
    assert progress.find(f'{XHTML}div[@class="track"]') is not None
    times = progress.findall(f'.//{XHTML}div[@class="times"]') + progress.findall(f'.//{XHTML}span[@class="times"]')
    assert current in " ".join(" ".join(node.itertext()) for node in times)
    total_label = times[-1][-1] if len(times) == 1 else times[-1]
    assert total_label.text == total
    assert f"width: {width}%;" in svg
    assert ('class="clock"' in svg) == animated


@pytest.mark.parametrize("theme", TIMELINE_THEMES)
def test_all_theme_timelines_hidden_offline(render_spotify, theme):
    root, svg = render_spotify(theme=theme, is_now_playing=False, show_offline=True)
    assert root.find(f'.//{XHTML}div[@class="track"]') is None
    assert 'class="clock"' not in svg


@pytest.mark.parametrize("theme,cover,height", [
    ("default", True, "478"), ("default", False, "178"),
    ("compact", True, "433"), ("compact", False, "133"),
    ("karaoke", True, "478"), ("karaoke", False, "178"),
    ("natemoo-re", True, "117"), ("natemoo-re", False, "117"),
    ("novatorem", True, "133"), ("novatorem", False, "133"),
])
def test_legacy_timelines_have_room_below_content(render_spotify, theme, cover, height):
    root, _ = render_spotify(theme=theme, cover_image=cover)
    assert root.get("height") == height
    assert root.find("{http://www.w3.org/2000/svg}foreignObject").get("height") == height


def test_spotify_elapsed_clock_scales_by_minutes_for_long_tracks(render_spotify):
    root, svg = render_spotify(progress_ms=0, duration_ms=10800000, cover_image=False)
    assert _clock_label_at(root, 6000) == "100:00"
    assert _clock_label_at(root, 10801) == "180:00"
    assert len(svg.encode("utf-8")) < 60000


@pytest.mark.parametrize("cover,height", [(True, "336"), (False, "114")])
def test_spotify_album_offline_shrinks(render_spotify, cover, height):
    root, _ = render_spotify(theme="spotify-album", cover_image=cover, is_now_playing=False, show_offline=True)
    assert root.get("height") == height


def test_spotify_album_missing_cover_shrinks(render_spotify):
    root, _ = render_spotify(theme="spotify-album", img="")
    assert root.get("height") == "128"
    assert root.find(f".//{XHTML}img") is None


@pytest.mark.parametrize("theme", SPOTIFY_THEMES)
@pytest.mark.parametrize("offline", [True, False])
@pytest.mark.parametrize("style,expected", [("spectrum", "spectrum"), ("invalid", "bars"), ("", "bars")])
def test_spotify_query_equalizer_and_default_color(client, theme, offline, style, expected):
    item = {"name": "Time To Pretend", "artists": [{"name": "Lazer Boomerang"}], "currently_playing_type": "track"}
    song = (None, False, None, None) if offline else (item, True, 196000, 314000)
    with patch("api.view.get_song_info", return_value=song):
        response = client.get(f"/?uid=test&theme={theme}&cover_image=false&eq_style={style}")
    assert response.status_code == 200 and response.mimetype == "image/svg+xml"
    svg = response.get_data(as_text=True)
    assert "color: #1ed760;" in svg
    if offline:
        assert "NOT PLAYING" in svg and '<span class="eq ' not in svg
    else:
        assert f'class="eq eq-{expected}"' in svg


@pytest.mark.parametrize("theme", SPOTIFY_THEMES)
def test_spotify_query_custom_bar_color(client, theme):
    item = {"name": "Song", "artists": [{"name": "Artist"}]}
    with patch("api.view.get_song_info", return_value=(item, True, 120000, 240000)):
        response = client.get(f"/?uid=test&theme={theme}&cover_image=false&bar_color=abcdef")
    assert "color: #abcdef;" in response.get_data(as_text=True)


@pytest.mark.parametrize("theme", SPOTIFY_THEMES)
def test_spotify_query_cover_bar_color(client, theme):
    import io
    from PIL import Image
    image = io.BytesIO()
    Image.new("RGB", (20, 20), (255, 0, 0)).save(image, format="PNG")
    item = {"name": "Song", "artists": [{"name": "Artist"}], "album": {"images": [{"url": "https://example.com/cover.png"}] * 3}}
    with patch("api.view.get_song_info", return_value=(item, True, 120000, 240000)), patch("api.view.load_image", return_value=image.getvalue()):
        response = client.get(f"/?uid=test&theme={theme}&bar_color_cover=true")
    assert "color: #ff0000;" in response.get_data(as_text=True)


def test_spotify_original_make_svg_call_still_works():
    from api.view import app, make_svg
    with app.app_context():
        svg = make_svg("Artist", "Song", "", True, False, "spotify-card", "1ed760", False, "121212", "light")
    assert 'class="eq eq-bars"' in svg


def test_spotify_text_is_xml_safe_and_truncated(render_spotify):
    root, svg = render_spotify(song_name='<script> & "Song" ' * 30, artist_name='Artist & Friends ' * 30)
    assert "<script>" not in svg
    assert root.find(f'.//{XHTML}div[@class="song"]').text.startswith('<script> & "Song"')
    assert "text-overflow: ellipsis" in svg
