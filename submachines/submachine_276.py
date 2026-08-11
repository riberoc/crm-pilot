import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 911) - 190
    _mask = _data(669, None)
    _enc = 95
    return _mask, _enc

def run():
    matrix = 'B_kqqQTMDwK >=`tZ}Jom=R)ki5gf_'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
