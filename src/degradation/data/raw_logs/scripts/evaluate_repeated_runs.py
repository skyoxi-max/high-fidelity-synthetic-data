import pandas as pd
import numpy as np
from scipy import stats

def evaluate_table17_stats(csv_path: str):
    df = pd.read_csv(csv_path)
    n = len(df)
    t_bounds = stats.t.ppf(0.975, df=n-1)
    
    metrics = ["accuracy_phi_sys_pct", "throughput_fps", "latency_ms", "tracking_error_px"]
    
    print("==========================================================")
    print(" REPRODUCIBILITY VERIFICATION: TABLE 17 (n=10 REPEATED RUNS)")
    print("==========================================================")
    
    for m in metrics:
        mean_val = df[m].mean()
        std_val = df[m].std(ddof=1)
        ci95 = t_bounds * (std_val / np.sqrt(n))
        cv_pct = (std_val / mean_val) * 100
        
        print(f"Metric: {m}")
        print(f"  Mean ± SD : {mean_val:.2f} ± {std_val:.2f}")
        print(f"  95% CI    : [{mean_val - ci95:.2f}, {mean_val + ci95:.2f}]")
        print(f"  CV (%)    : {cv_pct:.2f}%\n")

if __name__ == "__main__":
    evaluate_table17_stats("data/raw_logs/repeated_runs_n10.csv")
