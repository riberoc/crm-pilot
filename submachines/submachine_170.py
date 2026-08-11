import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 315) - 261
    _mask = _data(77, None)
    _enc = 98
    return _mask, _enc

def run():
    matrix = 'vhac=`Qzmuz2;zu7*@le9BT.9g_hYR'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
