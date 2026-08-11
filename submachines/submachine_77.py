import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 719) - 263
    _mask = _data(789, None)
    _enc = 210
    return _mask, _enc

def run():
    matrix = 'm W*)gSD}$A~p88!8U|PDBZ?m?1[8%'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
