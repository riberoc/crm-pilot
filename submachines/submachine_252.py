import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 215) - 848
    _mask = _data(1237, None)
    _enc = 178
    return _mask, _enc

def run():
    matrix = ' Ad|#!/)P8xOlHtuDwRPnikjTWc}TL'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
