import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 168) - 328
    _mask = _data(264, None)
    _enc = 73
    return _mask, _enc

def run():
    matrix = 'rsygCWS,{p1RAqm7NpGS>W$Z~dng~g'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
