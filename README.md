[README.md](https://github.com/user-attachments/files/29054095/README.md)
# Student Attendance Tracker

This project implements a complete data pipeline that generates raw session attendance data, cleans it, calculates student attendance metrics, determines certification eligibility, and visualizes the results.

## Project Overview

The pipeline processes 40 individual session CSV files to track student participation. A student is certified if they meet specific attendance thresholds based on their participation time in each session.

## Folder Structure

```
project/
│
├── raw-session-data/           # 40 raw CSV files (session_01.csv to session_40.csv)
├── preprocessed-session-data/  # 40 cleaned and aggregated CSV files
├── final.csv                   # Final attendance and certification report
├── scatter_attendance.png      # Visualization of classes attended per student
├── bar_certification.png       # Summary of certification counts
├── generate_raw_data.py        # Script for Phase 1 (Data Generation)
├── preprocess_data.py          # Script for Phase 2 (EDA & Cleaning)
├── calculate_attendance.py     # Script for Phase 3 & 4 (Analysis & Reporting)
├── visualize_results.py        # Script for Phase 5 (Visualization)
└── sample.csv                  # Original sample data used as a template
```

## Attendance Rules

1.  **Session Credit**: A student receives credit for a session if their total participation duration (`duration_min`) is ≥ 50% of the total session duration (60 minutes for a 120-minute session).
2.  **Certification Threshold**: A student is marked as **Certified** if they have valid attendance in at least 34 out of the 40 total sessions (80% threshold).

## Installation

Ensure you have Python 3 installed along with the required libraries:

```bash
pip install pandas matplotlib
```

## Running the Pipeline

The pipeline consists of five phases, each with its own script:

1.  **Phase 1: Generate Raw Data**
    ```bash
    python3 generate_raw_data.py
    ```
    Creates 40 mock session files in `raw-session-data/` starting from the first Monday of May 2026.

2.  **Phase 2: Preprocessing**
    ```bash
    python3 preprocess_data.py
    ```
    Cleans the raw data, handles duplicates, and aggregates student durations into `preprocessed-session-data/`.

3.  **Phase 3 & 4: Attendance Calculation & Report**
    ```bash
    python3 calculate_attendance.py
    ```
    Calculates attendance counts and generates the `final.csv` report.

4.  **Phase 5: Visualizations**
    ```bash
    python3 visualize_results.py
    ```
    Generates `scatter_attendance.png` and `bar_certification.png`.
