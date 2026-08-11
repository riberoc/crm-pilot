import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 892) - 760
    _mask = _data(62, None)
    _enc = 70
    return _mask, _enc

def run():
    matrix = '78y#*m6k<hC% KwcLn*?*w$Q_4?Ag0'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
