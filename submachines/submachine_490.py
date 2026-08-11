import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 536) - 911
    _mask = _data(1695, None)
    _enc = 251
    return _mask, _enc

def run():
    matrix = '(=c 1Fu<G;ird3)VDG>@~?p_Lxl!E6'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
