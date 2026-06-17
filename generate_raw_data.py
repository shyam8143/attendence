import csv
import random
from datetime import datetime, timedelta
import os

def generate_random_time(date_obj, start_hour, end_hour):
    start_time = date_obj.replace(hour=start_hour, minute=0, second=0)
    end_time = date_obj.replace(hour=end_hour, minute=0, second=0)

    # Total session duration is 120 mins (17:00 to 19:00)
    # Random join between 17:00 and 18:50
    random_join = start_time + timedelta(seconds=random.randint(0, 110 * 60))
    # Random leave between join and 19:00
    max_stay = int((end_time - random_join).total_seconds())
    random_leave = random_join + timedelta(seconds=random.randint(0, max_stay))

    duration = int((random_leave - random_join).total_seconds() / 60)
    return random_join.strftime('%-m/%-d/%Y %H:%M'), random_leave.strftime('%-m/%-d/%Y %H:%M'), duration

def main():
    os.makedirs('raw-session-data', exist_ok=True)

    with open('sample.csv', 'r', encoding='utf-8-sig') as f:
        reader = list(csv.reader(f))
        header = reader[0]
        template_rows = reader[1:]

    # First Monday of May 2026 is May 4th
    start_date = datetime(2026, 5, 4)

    session_dates = []
    current_date = start_date
    while len(session_dates) < 40:
        if current_date.weekday() != 6: # Skip only Sunday
            session_dates.append(current_date)
        current_date += timedelta(days=1)

    responses = ["OK", "No Response", ""]

    for i, session_date in enumerate(session_dates):
        filename = f'raw-session-data/session_{i+1:02d}.csv'

        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)

            for row in template_rows:
                if not any(row): # Empty row
                    writer.writerow(row)
                    continue

                new_row = list(row)

                # Vary only: creation_time (15), join_time (18), leave_time (19), duration_min (20), recording_disclaimer_response (22)

                # creation_time (15)
                creation_date = session_date - timedelta(days=random.randint(1, 20))
                new_row[15] = creation_date.strftime('%-m/%-d/%Y %H:%M')

                # join_time (18), leave_time (19), duration_min (20)
                join_t, leave_t, duration = generate_random_time(session_date, 17, 19)
                new_row[18] = join_t
                new_row[19] = leave_t
                new_row[20] = str(duration)

                # recording_disclaimer_response (22)
                new_row[22] = random.choice(responses)

                writer.writerow(new_row)

if __name__ == '__main__':
    main()
