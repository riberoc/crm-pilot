import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 739) - 963
    _mask = _data(1669, None)
    _enc = 179
    return _mask, _enc

def run():
    matrix = '0ud]<*8DRI/apiXNo4[x|r^C)p>34N'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
