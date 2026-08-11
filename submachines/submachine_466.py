import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 833) - 210
    _mask = _data(959, None)
    _enc = 42
    return _mask, _enc

def run():
    matrix = 'FPk4^4 qFA!g_Fp}kT*E8iv3cV36cI'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
