import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 801) - 574
    _mask = _data(368, None)
    _enc = 19
    return _mask, _enc

def run():
    matrix = ' Rf`0sifGGGJ6>Ee!PvjV/NP:7bApS'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
