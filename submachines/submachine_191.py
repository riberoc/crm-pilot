import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 965) - 459
    _mask = _data(472, None)
    _enc = 66
    return _mask, _enc

def run():
    matrix = '?KIfPS*2YIpMkqvP Nt,WW$evPgu!3'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
