import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 456) - 908
    _mask = _data(525, None)
    _enc = 50
    return _mask, _enc

def run():
    matrix = '^J3>MnYz%Z4cd*<_teJ`O+5$$>&R.e'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
