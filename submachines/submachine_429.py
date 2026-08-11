import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 877) - 859
    _mask = _data(142, None)
    _enc = 133
    return _mask, _enc

def run():
    matrix = 'LvibKU2djTMS8 mSTgOe&v;_b~zmMf'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
