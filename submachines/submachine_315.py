import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 798) - 160
    _mask = _data(617, None)
    _enc = 218
    return _mask, _enc

def run():
    matrix = '_H:1rAV-EibXp dykr0L#aFWO5!]MX'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
