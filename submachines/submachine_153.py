import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 977) - 451
    _mask = _data(381, None)
    _enc = 244
    return _mask, _enc

def run():
    matrix = '/)BXs:+&Q!!0Pmc;~nf$5si8xxj?` '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
