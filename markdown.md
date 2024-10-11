# This is a simple project that analyzes a dataset of medical insurance costs. The dataset contains the following columns:
# ['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']

## Output

### The average age of this dataset is:
| 39.2 |

### Majority of the individuals in descending order are from:
| Region    | Individuals |
|-----------|--------------|
| Southeast | 364          |
| Southwest | 325          |
| Northwest | 325          |
| Northeast | 324          |

### Average insurance charges by region:
| Region    | Average Charges |
|-----------|------------------|
| Southwest | 12346.9          |
| Southeast | 14735.4          |
| Northwest | 12417.6          |
| Northeast | 13406.4          |

### The average BMI:
| Gender | BMI  |
|--------|------|
| Males  | 30.9 |
| Females| 30.4 |

### The average age based on having children:
| Condition                | Average Age |
|--------------------------|-------------|
| At least one child       | 39.8        |
| No children              | 38.4        |

### The average cost for smokers vs non-smokers:
| Condition   | Average Cost | Difference |
|-------------|--------------|------------|
| Smokers     | 32050.0$     |            |
| Non-smokers | 8434.0$      | 23616.0$   |

**Note:** The difference in average cost between smokers and non-smokers is **23616.0$** (WHICH IS HUGE!)