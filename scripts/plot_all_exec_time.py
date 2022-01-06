import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read innput
def read_instruct_csv_to_frame():
    return pd.read_csv(sys.stdin)

def parse_test_names(df):
    df[['fft','type', 'size']] = df['test'].str.split('_', expand=True)
    df = df.drop(['test'], axis=1)
    df['size'] = df['size'].astype(int)
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

    file_name = file_name + "riscv-execution-time.png"
    plt.savefig(file_name, dpi=300, bbox_inches='tight')


def normalize(df):
    grouped_df = df.groupby(['size'])['time_us @200MHz']
    df['norm'] = grouped_df.transform(lambda x : x / x.max())
    return df

    
def plot_all_exec_times_norm(file_name, df):

    fft_size = ['64', '128', '256', '512', '1024', '2048', '4096']
    labels = fft_size

    # Remove size 8192
    df = df[df['size'] < 8192]


    ## Time based plot all
    cfft_f32_exec_times = df.loc[
            (df['fft'] == "cfft") &
            (df['type'] == "f32"), 
            "norm" ]
    cfft_q31_exec_times = df.loc[
            (df['fft'] == "cfft") &
            (df['type'] == "q31"),
            "norm" ]
    cfft_q15_exec_times = df.loc[
            (df['fft'] == "cfft") &
            (df['type'] == "q15"),
            "norm" ]
    rfft_f32_exec_times = df.loc[
            (df['fft'] == "rfft") &
            (df['type'] == "f32"),
            "norm" ]
    rfft_q31_exec_times = df.loc[
            (df['fft'] == "rfft") &
            (df['type'] == "q31"),
            "norm" ]
    rfft_q15_exec_times = df.loc[
            (df['fft'] == "rfft") &
            (df['type'] == "q15"),
            "norm" ]

    width = 0.10  # the width of the bars
    x = np.arange(len(labels))  # the label locations

    fig, ax = plt.subplots()
    ax.grid(zorder=0)

    #### Create bars
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
    ax.set_ylabel('Execution time normalized')
    ax.set_title('Normalized dynamic execution time of RISC-V FFT functions')
    ax.set_xticks(x, labels)
    ax.legend(bbox_to_anchor=(1.0, 1.00))
    fig.tight_layout()

    file_name = file_name + "riscv-execution-norm.png"
    plt.savefig(file_name, dpi=300, bbox_inches='tight')



def plot_norm_line_chart(file_name, df):
    fft_size = ['64', '128', '256', '512', '1024', '2048', '4096']
    labels = fft_size

    # Remove size 8192
    df = df[df['size'] < 8192]


    ## Time based plot all
    cfft_f32_exec_times = df.loc[
            (df['fft'] == "cfft") &
            (df['type'] == "f32"), 
            "norm" ]
    cfft_q31_exec_times = df.loc[
            (df['fft'] == "cfft") &
            (df['type'] == "q31"),
            "norm" ]
    cfft_q15_exec_times = df.loc[
            (df['fft'] == "cfft") &
            (df['type'] == "q15"),
            "norm" ]
    rfft_f32_exec_times = df.loc[
            (df['fft'] == "rfft") &
            (df['type'] == "f32"),
            "norm" ]
    rfft_q31_exec_times = df.loc[
            (df['fft'] == "rfft") &
            (df['type'] == "q31"),
            "norm" ]
    rfft_q15_exec_times = df.loc[
            (df['fft'] == "rfft") &
            (df['type'] == "q15"),
            "norm" ]



    x = np.arange(len(labels))  # the label locations
    fig, ax = plt.subplots()
    ax.grid(zorder=0)

    ax.plot(fft_size, rfft_f32_exec_times, label="rfft f32", zorder=4, linewidth=4)
    ax.plot(fft_size, rfft_q31_exec_times, label="rfft q31", zorder=4, linewidth=4)
    ax.plot(fft_size, rfft_q15_exec_times, label="rfft q15", zorder=4, linewidth=4)
    ax.plot(fft_size, cfft_f32_exec_times, label="cfft f32", zorder=4, linewidth=4)
    ax.plot(fft_size, cfft_q31_exec_times, label="cfft q31", zorder=4, linewidth=4)
    ax.plot(fft_size, cfft_q15_exec_times, label="cfft q15", zorder=4, linewidth=4)

    ax.set_xlabel('FFT size')
    ax.set_ylabel('Execution time normalized')
    ax.set_title('Line Normalized dynamic execution time of RISC-V FFT functions')
    ax.set_xticks(x, labels)
    ax.legend(bbox_to_anchor=(1.0, 1.00))
    fig.tight_layout()

    file_name = file_name + "riscv-execution-norm-line.png"
    plt.savefig(file_name, dpi=300, bbox_inches='tight')


def plot_multi_barchart(df_pivot,title, y_label, file_name):
    ax = df_pivot.plot(kind='bar', zorder=4, title=title)
    ax.set(ylabel = y_label)
    ax.grid(zorder=0)
    plt.savefig(file_name, dpi=300, bbox_inches='tight')


def plot_comparison(filepath, riscv_df, dsp_df):

    # Prepare dsp dataframe
    dsp_df = dsp_df[['DSP', 'FFT-type', 'FFT points', 'Execution time [µs]']]

    dsp_df[['fft','type']] = dsp_df['FFT-type'].str.split('-', expand=True)
    dsp_df = dsp_df.drop(['FFT-type'], axis=1)

    dsp_df = dsp_df.rename(columns={"Execution time [µs]":"time_us",
                                    "DSP": "Name"})

    # Prepare riscv dataframe
    riscv_df = riscv_df[['time_us @200MHz', 'fft', 'type', 'size']]
    riscv_df['Name'] = "rv32imfc"
    riscv_df = riscv_df.rename(columns={"time_us @200MHz":"time_us",
                                        "size": "FFT points"})
    # Merge the two dataframes
    df = dsp_df.append(riscv_df)
    df['fft-type'] = df['fft'] + "-" + df['type']

    

    grouped = df.groupby(['FFT points', 'fft', 'type'])
    df['norm'] = grouped['time_us'].transform(lambda x : x / x.max())
    df['performance'] = 1 / df['norm']


    df_rfft_q15 = df[(df['fft'] == 'rfft') & (df['type'] == 'q15') & (df['FFT points'] > 256)]
    df_cfft_q31 = df[(df['fft'] == 'cfft') & (df['type'] == 'q31')]
    df_cfft_f32 = df[(df['fft'] == 'cfft') & (df['type'] == 'f32')]

    df_to_plot = [df_rfft_q15, df_cfft_q31, df_cfft_f32]

    # Plot performance and ratio
    for dfp in df_to_plot:
        fft_type = dfp['fft-type'].iloc[0]
        dfpiv = dfp.pivot(index='FFT points', columns='Name', values='performance')
        plot_multi_barchart(dfpiv, 
                            "Relative performance of " + fft_type, 
                            "Relative performance", 
                            filepath + "relative-performance-" + fft_type + ".png")

        dfpiv = dfp.pivot(index='FFT points', columns='Name', values='norm')
        plot_multi_barchart(dfpiv, 
                            "Normalized ratio of " + fft_type, 
                            "Ratio of slowest", 
                            filepath + "relative-ratio-" + fft_type + ".png")


def main(file_name):
    df = read_instruct_csv_to_frame()
    df = parse_test_names(df)
    df = normalize(df)

    plot_all_exec_times(file_name, df)
    plot_all_exec_times_norm(file_name, df)
    plot_norm_line_chart(file_name, df)

    dsp_df = pd.read_csv("dsp-benchmarks.csv")
    plot_comparison(file_name, df, dsp_df)


if __name__ == "__main__":
    main(sys.argv[1])
