import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 446) - 522
    _mask = _data(829, None)
    _enc = 96
    return _mask, _enc

def run():
    matrix = ']-l@p?i+WurZ9-0ct<N=(&OtN ;]:['
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
