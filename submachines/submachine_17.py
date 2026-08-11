import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 815) - 102
    _mask = _data(553, None)
    _enc = 188
    return _mask, _enc

def run():
    matrix = 'g#d~h6Av~j(m]2(|;I=R|WTsQz4w W'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
