import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 313) - 874
    _mask = _data(682, None)
    _enc = 40
    return _mask, _enc

def run():
    matrix = 'D kE,gm;]*OcX=utf=,X{}+}kQ4PD$'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
