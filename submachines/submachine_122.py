import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 977) - 650
    _mask = _data(269, None)
    _enc = 91
    return _mask, _enc

def run():
    matrix = '`e3r@G.&~ [s1hUAG5m+0|=QBmq%UM'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
