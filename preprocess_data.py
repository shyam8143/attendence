import pandas as pd
import os
import glob

def preprocess_file(input_path, output_path):
    # Using low_memory=False and engine='python'
    df = pd.read_csv(input_path, engine='python')

    # Names of interest based on sample.csv
    name_col = 'Name (original name)'
    email_col = 'Email'

    # Handle potentially duplicated column names by index
    # We want the 21st column (index 20) which is participant Duration (minutes)
    p_duration_val = df.iloc[:, 20]

    # Create a new df with just what we need
    new_df = pd.DataFrame({
        'student_name': df[name_col],
        'student_email': df[email_col],
        'duration_min': pd.to_numeric(p_duration_val, errors='coerce').fillna(0)
    })

    # Clean data
    new_df = new_df.dropna(subset=['student_name', 'student_email'], how='all')
    new_df = new_df[new_df['student_name'] != 'Name (original name)']

    # Aggregate by Email (since names can vary slightly for same person)
    # Actually, keep name for the report
    clean_df = new_df.groupby(['student_email'], as_index=False).agg({
        'student_name': 'first',
        'duration_min': 'sum'
    })

    # Reorder columns
    clean_df = clean_df[['student_name', 'student_email', 'duration_min']]

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    clean_df.to_csv(output_path, index=False)

def main():
    input_files = sorted(glob.glob('raw-session-data/session_*.csv'))
    for f in input_files:
        basename = os.path.basename(f)
        preprocess_file(f, f'preprocessed-session-data/{basename}')
        print(f'Preprocessed {basename}')

if __name__ == '__main__':
    main()
