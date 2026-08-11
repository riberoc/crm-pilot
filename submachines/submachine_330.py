import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 445) - 398
    _mask = _data(906, None)
    _enc = 172
    return _mask, _enc

def run():
    matrix = '{P:l*d-0[m_CAY;W/}axrr1s_2koG6'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
