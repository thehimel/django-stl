"""Test utilities"""
from core.utilities import extract
from pathlib import Path


def test_extract_square():
    """Test extract for square sphere."""
    file = Path("src/core/tests/files/rectangle.STL").absolute()
    output = extract(file=file, sphere_type=1)
    expected = {'width': 24.45372, 'length': 78.18404, 'height': 22.46212, 'volume': 42945.114583333336, 'surface_area': 8434.705}
    assert sorted(output) == sorted(expected)


def test_extract_round():
    """Test extract for round sphere."""
    file = Path("src/core/tests/files/300_polygon_sphere_100mm.STL").absolute()
    output = extract(file=file, sphere_type=2)
    expected = {'length': 78.74016, 'diameter': 78.42971, 'volume': 248787.6444042185, 'surface_area': 19215.902}
    assert sorted(output) == sorted(expected)


def test_extract_round_invalid():
    """Test extract for invalid round sphere"""
    file = Path("src/core/tests/files/rectangle.STL").absolute()
    assert "error" in extract(file=file, sphere_type=2)
