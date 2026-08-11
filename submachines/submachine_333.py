import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 160) - 969
    _mask = _data(860, None)
    _enc = 53
    return _mask, _enc

def run():
    matrix = 'jGV;.u sj{}krXW6L{nt+:0kK$+0n;'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
