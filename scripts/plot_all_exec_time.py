import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read innput
def read_instruct_csv_to_frame():
    return pd.read_csv(sys.stdin)

def parse_test_names(df):
    test_case_names = df['test'].str.split('_', n=0, expand=True)
    df['fft'] = test_case_names[0]
    df['type'] = test_case_names[1]
    df['size'] = test_case_names[2]
    return df


def plot_all_exec_times(file_name, df):

    labels = ['64', '128', '256', '512', '1024', '2048', '4096', '8192']

    cfft_f32_exec_times = df.loc[
            (df['fft'] == "cfft") &
            (df['type'] == "f32"), 
            "time_us @200MHz" ]
    cfft_q31_exec_times = df.loc[
            (df['fft'] == "cfft") &
            (df['type'] == "q31"),
            "time_us @200MHz" ]
    cfft_q15_exec_times = df.loc[
            (df['fft'] == "cfft") &
            (df['type'] == "q15"),
            "time_us @200MHz" ]
    rfft_f32_exec_times = df.loc[
            (df['fft'] == "rfft") &
            (df['type'] == "f32"),
            "time_us @200MHz" ]
    rfft_q31_exec_times = df.loc[
            (df['fft'] == "rfft") &
            (df['type'] == "q31"),
            "time_us @200MHz" ]
    rfft_q15_exec_times = df.loc[
            (df['fft'] == "rfft") &
            (df['type'] == "q15"),
            "time_us @200MHz" ]

    zero_padding = pd.Series([0])
    cfft_f32_exec_times = cfft_f32_exec_times.append(zero_padding, ignore_index=True)
    cfft_q31_exec_times = cfft_q31_exec_times.append(zero_padding, ignore_index=True)
    cfft_q15_exec_times = cfft_q15_exec_times.append(zero_padding, ignore_index=True)
    rfft_f32_exec_times = rfft_f32_exec_times.append(zero_padding, ignore_index=True)


    x = np.arange(len(labels))  # the label locations
    width = 0.10  # the width of the bars

    fig, ax = plt.subplots()
    ax.grid(zorder=0)

    ### Create bars
    rects1 = ax.bar(x - 5 * width/2, rfft_f32_exec_times, width, label='rfft f32',
            zorder=4)
    rects2 = ax.bar(x - 3 * width/2,  rfft_q31_exec_times, width, label='rfft q31',
            zorder=4)
    rects3 = ax.bar(x - width/2, rfft_q15_exec_times, width, label='rfft q15', zorder=4)
    rects4 = ax.bar(x + width/2, cfft_f32_exec_times, width, label='cfft f32', zorder=4)
    rects5 = ax.bar(x + 3 * width/2, cfft_q31_exec_times, width, label='cfft q31',
            zorder=4)
    rects6 = ax.bar(x + 5 * width/2, cfft_q15_exec_times, width, label='cfft q15',
            zorder=4)

    ax.set_xlabel('FFT size')
    ax.set_ylabel('Execution time [µs]')
    ax.set_title('Dynamic execution time of RISC-V FFT functions')
    ax.set_xticks(x, labels)
    ax.legend()

    fig.tight_layout()

    #plt.show()
    plt.savefig(file_name, dpi=300, bbox_inches='tight')

def main(file_name):
    df = read_instruct_csv_to_frame()
    df = parse_test_names(df)
    plot_all_exec_times(file_name, df)


if __name__ == "__main__":
    main(sys.argv[1])
