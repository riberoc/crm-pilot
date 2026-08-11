import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 575) - 447
    _mask = _data(966, None)
    _enc = 63
    return _mask, _enc

def run():
    matrix = '^#*49 t_(@86/VUDBJjRwMKzWvnVvu'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
