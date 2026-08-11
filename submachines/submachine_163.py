import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 257) - 640
    _mask = _data(634, None)
    _enc = 254
    return _mask, _enc

def run():
    matrix = 'Vz%_rnHoa<F77o[6C#j`}duuZ}dYhm'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
