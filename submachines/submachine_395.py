import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 775) - 721
    _mask = _data(180, None)
    _enc = 247
    return _mask, _enc

def run():
    matrix = '|yu1HaK}68WsC!fmHc4:d oe&cptI`'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
