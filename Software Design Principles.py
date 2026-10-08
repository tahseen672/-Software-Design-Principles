"""
Functional programming example: grade statistics.

Design principles demonstrated:
- Single Responsibility: each function does exactly one job.
- Pure functions: no global state, no side effects. The same input
  always gives the same output, which makes them easy to test.
- DRY: the grade-to-letter logic lives in one place and is reused.
- Composition: small functions are combined to build bigger behaviour.
"""


def calculate_average(scores):
    """Return the average of a list of scores (0 if the list is empty)."""
    if not scores:
        return 0
    return sum(scores) / len(scores)


def find_highest(scores):
    """Return the highest score."""
    return max(scores)


def to_letter_grade(score):
    """Convert a numeric score to a letter grade."""
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def convert_all_to_letters(scores):
    """Reuse to_letter_grade for every score (composition + DRY)."""
    return [to_letter_grade(score) for score in scores]


def build_report(scores):
    """Combine the small functions above into one report (composition)."""
    average = calculate_average(scores)
    return {
        "average": round(average, 2),
        "highest": find_highest(scores),
        "average_letter": to_letter_grade(average),
        "letters": convert_all_to_letters(scores),
    }


# Only the entry point does printing (side effects are kept at the edge).
if __name__ == "__main__":
    student_scores = [85, 92, 78, 64, 99]
    print(build_report(student_scores))