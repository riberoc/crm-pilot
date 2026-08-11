import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 589) - 317
    _mask = _data(71, None)
    _enc = 198
    return _mask, _enc

def run():
    matrix = 'k|29|g0Ci!1 @*E&]R>L=0$?Lh#qF,'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
