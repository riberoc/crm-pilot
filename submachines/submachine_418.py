import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 380) - 297
    _mask = _data(44, None)
    _enc = 37
    return _mask, _enc

def run():
    matrix = 'C- gH.#b[~zA3aU{<CZn|}%9u]6i}K'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
