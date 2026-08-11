import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 842) - 878
    _mask = _data(1822, None)
    _enc = 245
    return _mask, _enc

def run():
    matrix = 'i79uG-VUX[*wT,7BT(za<o{Oiinn-j'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
