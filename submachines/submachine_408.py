import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 657) - 768
    _mask = _data(355, None)
    _enc = 229
    return _mask, _enc

def run():
    matrix = 'wPo>Z~uPB**|L6Q15%0{k@@ -$.)%z'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
