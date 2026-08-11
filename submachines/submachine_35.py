import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 224) - 355
    _mask = _data(293, None)
    _enc = 121
    return _mask, _enc

def run():
    matrix = 'FBSAsUhxl74~$(!@Ue)bRGV$;|O J8'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
