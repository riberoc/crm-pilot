import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 737) - 289
    _mask = _data(838, None)
    _enc = 132
    return _mask, _enc

def run():
    matrix = 'Vf 3(39HXuq`e++b]#$<s!B[f?p.HY'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
