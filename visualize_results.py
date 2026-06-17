import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('final.csv')

    # --- Plot 1: Scatter Plot ---
    plt.figure(figsize=(12, 6))

    # Separate certified and non-certified for coloring
    certified = df[df['classes_attended'] >= 34]
    not_certified = df[df['classes_attended'] < 34]

    plt.scatter(certified.index, certified['classes_attended'], color='green', label='Certified (>= 34)')
    plt.scatter(not_certified.index, not_certified['classes_attended'], color='red', label='Not Certified (< 34)')

    plt.xlabel('Student Index')
    plt.ylabel('Classes Attended')
    plt.title('Student Attendance Overview')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig('scatter_attendance.png')
    plt.close()

    # --- Plot 2: Bar Chart ---
    plt.figure(figsize=(8, 6))

    cert_count = len(certified)
    not_cert_count = len(not_certified)

    categories = ['Certified', 'Not Certified']
    counts = [cert_count, not_cert_count]
    colors = ['green', 'red']

    plt.bar(categories, counts, color=colors)
    plt.ylabel('Number of Students')
    plt.title('Certification Summary')

    # Add counts on top of bars
    for i, count in enumerate(counts):
        plt.text(i, count + 0.5, str(count), ha='center', va='bottom')

    plt.savefig('bar_certification.png')
    plt.close()

    print("Generated visualizations: scatter_attendance.png, bar_certification.png")

if __name__ == '__main__':
    main()
