# 📂 Data Dictionary & Pipeline
This directory houses the 200+ raw CSV sources and the resulting engineered datasets.

### 📊 Sources
* **Sports Reference:** Basic and Advanced school statistics (2012-2025).
* **EvanMiya:** Individual player BPR (Bayesian Performance Rating) and team rankings.
* **NBA Draft Data:** Prospect density metrics to identify elite talent pipelines.

### ⚙️ The Pipeline
1. **Normalization:** Used `rapidfuzz` to resolve team name discrepancies across different providers.
2. **Centralization:** Combined 14 years of stats into a SQLite (`bracket.db`) database for the Flask app.
3. **Imputation:** Handled missing values through mean-substitution and seed-based averages.