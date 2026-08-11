import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 296) - 433
    _mask = _data(855, None)
    _enc = 215
    return _mask, _enc

def run():
    matrix = '/PtK_IP-V=0h2%L;<dhYVE-nJ OVxR'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
