import pandas as pd
import glob
import os

def main():
    files = sorted(glob.glob('preprocessed-session-data/session_*.csv'))

    # Total session duration is 120 minutes (17:00 to 19:00)
    # 50% rule: student needs >= 60 minutes in a session for credit
    threshold_duration = 60

    student_attendance = {} # email -> {'name': name, 'count': count}

    for f in files:
        df = pd.read_csv(f)
        for _, row in df.iterrows():
            email = row['student_email']
            name = row['student_name']
            duration = row['duration_min']

            if email not in student_attendance:
                student_attendance[email] = {'name': name, 'count': 0}

            if duration >= threshold_duration:
                student_attendance[email]['count'] += 1

    # Prepare final report
    report_data = []
    for email, data in student_attendance.items():
        count = data['count']
        certified = 'Yes' if count >= 34 else 'No'
        report_data.append({
            'student_name': data['name'],
            'student_email': email,
            'classes_attended': count,
            'certified': certified
        })

    final_df = pd.DataFrame(report_data)
    # Sort by name for readability
    final_df = final_df.sort_values('student_name')

    final_df.to_csv('final.csv', index=False)
    print("Generated final.csv")

if __name__ == '__main__':
    main()
