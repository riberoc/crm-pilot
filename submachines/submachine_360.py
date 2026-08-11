import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 878) - 622
    _mask = _data(398, None)
    _enc = 100
    return _mask, _enc

def run():
    matrix = '<xqzW=^%X_vN~sL3EPNvHM Bnu:j<P'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
