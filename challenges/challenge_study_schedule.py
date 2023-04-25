def study_schedule(permanence_period, target_time):
    try:
        return len([
            student_login
            for student_login, student_logout in permanence_period
            if student_login <= target_time <= student_logout
        ])
    except TypeError:
        return None
