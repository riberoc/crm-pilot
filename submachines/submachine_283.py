import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 185) - 867
    _mask = _data(1183, None)
    _enc = 198
    return _mask, _enc

def run():
    matrix = '#=-8[ By(mt}4E$K;o6>V_^}<*IddY'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
