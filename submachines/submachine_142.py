import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 462) - 961
    _mask = _data(1455, None)
    _enc = 161
    return _mask, _enc

def run():
    matrix = 'v aQo%,:?z(bS+zSISadR0Hh3I(&w]'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
