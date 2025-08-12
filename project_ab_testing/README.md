
# Project: A/B Test Analysis for a Marketing Campaign

This project provides a concise, end-to-end analysis of a classic A/B test. The goal is to determine with statistical confidence whether a new ad campaign was more effective at converting users than a control (a public service announcement).

### The Analytical Process

A formal hypothesis testing framework was used to ensure a rigorous and unbiased conclusion:

1.  **Hypothesis Formulation:** A clear null hypothesis (no difference in conversion rates) and alternative hypothesis (the ad's conversion rate is higher) were defined.
2.  **Data Preparation:** The data was cleaned and the observed conversion rates were calculated (2.55% for the ad group vs. 1.78% for the control group).
3.  **Statistical Test:** A **Chi-Squared Test of Independence** was performed to determine if the observed difference was statistically significant.

### Conclusion & Recommendation

The test yielded a **p-value of < 0.0001**, which is well below the standard significance level of 0.05.

**Result:** We **reject the null hypothesis**. The analysis provides strong statistical evidence that the ad campaign was effective at increasing user conversions. A final financial analysis based on reasonable assumptions also showed a positive Return on Ad Spend (ROAS).

**Recommendation:** The company should proceed with the full rollout of the ad campaign.

**The full analysis can be found in the notebook:**
*   [View the Notebook](./AB_Test_Analysis.ipynb)
*   [View the Clean HTML Report](https://htmlpreview.github.io/?https://raw.githubusercontent.com/jalhane88/Data-Analysis-Portfolio/refs/heads/main/project_ab_testing/AB_Test_Analysis.html)
