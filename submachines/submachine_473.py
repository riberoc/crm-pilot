import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 735) - 945
    _mask = _data(258, None)
    _enc = 40
    return _mask, _enc

def run():
    matrix = ')S>3 Ez#6nt8T@UQ_E/_VO)m_W_x!8'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
