import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 905) - 147
    _mask = _data(869, None)
    _enc = 89
    return _mask, _enc

def run():
    matrix = 'yMh`);/J2g~]}VG&&|XS*DaFq{T<h]'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
