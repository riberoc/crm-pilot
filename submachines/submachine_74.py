import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 385) - 845
    _mask = _data(1415, None)
    _enc = 162
    return _mask, _enc

def run():
    matrix = 'F;6}Ve;7P@Ap6B8Wx_F)37qUv6_ 9]'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
