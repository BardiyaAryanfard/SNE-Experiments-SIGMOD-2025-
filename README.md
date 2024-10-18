Repository for codes corresponding to the experiments of the paper: "Private and Simultaneous Estimation of Symmetric Norms under Continual Observation" submission to SIGMOD 2025

All codes in Python 3.12

This file contains a brief explanation on the files in this repository.

.
├── SNE experiment/
│   ├── src/
│   │   ├── algorithms/
│   │   │   └── General_Norm.py
│   │   ├── non_private/
│   │   │   └── norms.py
│   │   ├── test_generator/
│   │   └── util/
│   ├── files/  # Contains the processed version of the input files cited in the paper and the artificial datasets used to find the best heuristic improvement.
│   │   │          In these files, the elements are named by the order of their appearance in the original dataset. The files contain the sequence of the insertions.         
│   │   └── test/ # Outputs for 5 independent runs of all of the datasets.
├── index.html
└── README.md  # This file
