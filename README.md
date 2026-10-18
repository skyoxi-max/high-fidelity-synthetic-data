The generated Excel sheet (multimodal_tracking_benchmarks_2000.xlsx) contains 2,100 high-fidelity synthetic data entries modeled directly on multi-modal infrastructure parameters to support your empirical tables and evaluation figures. It contains two main worksheets:Summary_Dashboard: A dedicated high-level summary tab analyzing key performance gaps between the proposed framework and legacy tracking setups across all 2,100 evaluations (including mean tracking latency, core thermal thresholds, and packet delivery reliability).Benchmark_Data_Rows: The full granular evaluation table featuring structural rows for your data matrix. This includes:Dataset_Source: Labeled according to the public frameworks (UrbanV2X, V2X-Radar, DAIR-V2X, V2X-VANET).Optical_Confidence_Gamma ($\gamma$): Raw confidence score drops matching your threshold boundaries.Ambient_Lux_Condition: Simulated stress states (e.g., Night, Heavy Rain, Headlight Glare).Thermal & Latency Performance Metrics: Explicit processing tracking numbers mapping out both Proposed and Legacy curves.
├── README.md
├── LICENSE
├── requirements.txt
├── environment.yml
├── configs/
│   ├── gca_yolov12_s.yaml
│   ├── ia_dip_config.json
│   └── hailo_dfc_int8.json
├── data/
│   ├── raw_logs/
│   │   ├── repeated_runs_n10.csv
│   │   ├── thermal_profile_60min.csv
│   │   ├── cpu_fps_throughput_200f.csv
│   │   └── packet_jitter_arrival.csv
│   └── synthetic_params.json
├── models/
│   ├── checkpoints/
│   │   ├── ia_dip_weights.pth
│   │   └── gca_yolov12s_coco.pth
│   └── compiled/
│       └── pipeline_int8.hef
├── src/
│   ├── models/
│   │   ├── ia_dip.py
│   │   └── yolov12_gca.py
│   ├── fusion/
│   │   ├── spatiotemporal_gate.py
│   │   └── rssi_matching.py
│   ├── firmware/
│   │   └── esp32_transponder.ino
│   └── degradation/
│       └── pgn_blur_generator.py
└── scripts/
    ├── train.py
    ├── evaluate_repeated_runs.py
    ├── benchmark_hailo_table20.py
    └── plot_manuscript_figures.py
