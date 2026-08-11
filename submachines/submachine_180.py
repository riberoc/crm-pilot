import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 101) - 549
    _mask = _data(763, None)
    _enc = 110
    return _mask, _enc

def run():
    matrix = 'F`l.)pZ[k4VkxK6^.Ptltr` [).cFp'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
