import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 636) - 727
    _mask = _data(344, None)
    _enc = 80
    return _mask, _enc

def run():
    matrix = '@vE2amYau<)9]_<lFSodjzVj6pCgg '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
