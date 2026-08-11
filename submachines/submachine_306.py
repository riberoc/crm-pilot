import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 188) - 921
    _mask = _data(861, None)
    _enc = 78
    return _mask, _enc

def run():
    matrix = 'o:M9.x uo|gKK-`e#+Q`*[Zh@IruRb'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
