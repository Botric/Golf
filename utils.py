# utils.py
def compute_course_handicap(handicap_index: float, slope: int) -> int:
    return int(round(handicap_index * (slope / 113)))
