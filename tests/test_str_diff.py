import pytest
from src.str_diff import get_diff


@pytest.mark.parametrize(
    "first_str, second_str, expected_diff",
    [
        ("SAMAT", "SAMSAMAN", [([0, 1, 2, 3], [3, 4, 5, 6])]),
        ("Y1233345", "128845w", [([1, 2], [0, 1]), ([6, 7], [4, 5])]),
        (
            "Some really long string that has a couple of differences.",
            "Some rlly long string thathas a couple of differences.",
            [
                ([0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]),
                (
                    [
                        8,
                        9,
                        10,
                        11,
                        12,
                        13,
                        14,
                        15,
                        16,
                        17,
                        18,
                        19,
                        20,
                        21,
                        22,
                        23,
                        24,
                        25,
                        26,
                        27,
                    ],
                    [
                        6,
                        7,
                        8,
                        9,
                        10,
                        11,
                        12,
                        13,
                        14,
                        15,
                        16,
                        17,
                        18,
                        19,
                        20,
                        21,
                        22,
                        23,
                        24,
                        25,
                    ],
                ),
                (
                    [
                        35,
                        36,
                        37,
                        38,
                        39,
                        40,
                        41,
                        42,
                        43,
                        44,
                        45,
                        46,
                        47,
                        48,
                        49,
                        50,
                        51,
                        52,
                        53,
                        54,
                        55,
                        56,
                    ],
                    [
                        32,
                        33,
                        34,
                        35,
                        36,
                        37,
                        38,
                        39,
                        40,
                        41,
                        42,
                        43,
                        44,
                        45,
                        46,
                        47,
                        48,
                        49,
                        50,
                        51,
                        52,
                        53,
                    ],
                ),
            ],
        ),
    ],
)
def test_get_diff_correctly_identifies_differences_in_strings(
    first_str, second_str, expected_diff
):
    difference = get_diff(first_str, second_str)
    assert difference == expected_diff
