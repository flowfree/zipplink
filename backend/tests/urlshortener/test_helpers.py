from apps.urlshortener.helpers import Base62


def test_encode_number():
    tests = [
        (100, '1C'),
        (200, '3e'),
        (31245, '87X'),
        (54321, 'e89'),
        (31227065, '271Al'),
    ]
    for x, y in tests:
        assert Base62.encode(x) == y


def test_decode_string():
    tests = [
        ('1C', 100),
        ('3e', 200),
        ('87X', 31245),
        ('e89', 54321),
        ('271Al', 31227065),
    ]
    for x, y in tests:
        assert Base62.decode(x) == y
