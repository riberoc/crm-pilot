import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 389) - 802
    _mask = _data(551, None)
    _enc = 156
    return _mask, _enc

def run():
    matrix = ')edtTX!<n]AOJqs<D0kjlz?m.Z~c g'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
