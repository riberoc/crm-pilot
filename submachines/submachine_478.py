import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 576) - 236
    _mask = _data(897, None)
    _enc = 198
    return _mask, _enc

def run():
    matrix = '0+r#[dn2!c^X[j/UQi{ E}1s7}C3H5'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
