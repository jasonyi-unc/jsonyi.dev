---
layout: summary
title: "Interpretable Machine Learning: Fundamental Principles and 10 Grand Challenges"
date: 2024-09-15
giscus_comments: true
bib_id: 2103.11251v2
---

*Currently in Progress*

### Vocabulary
Some important terms that frequently pop up during the paper:
* **tablular data**: all variables are real or discrete features, each of which is meaningful (age, race, sex, congestive heart failure, etc)
* **raw data**: images (pixels), sound files, text (words)
* **Rashomon set**: group of approximately-equally-good models to black box models
* **sparsity**: measure of interpretability for tabular data where the features are meaningful
    * makes it useful to troubleshoot, check for typographical errors, and reason about counterfactuals
        * "How would my prediction change if I changed this specific input?"
* **logical models**: models that consist of logical statements involving "if-then", "or", & "and" clauses
    * good for modeling categorical data with potentially complicated interaction terms and for multiclass problems
    * key examples include a decision tree, decision list, and a decision set
* **continuous variable**: feature that takes an infinite number of values in a given range, e.g. age, height, or temperature
* **scoring systems**: linear classification models that require users to add, subtract, and multiply only a few small numbers to make a prediction
    * commonly use binary/indicator variables (e.g. age $$\geq$$ 60) and point values to make score computations easier
    * used to access the risk of numerous serious medical conditons due to its quick predictions without the use of a computer


### The Problem With Black Box Models

A black box machine learning model is a formula that is either too complicated for humans to understand, or proprietary, so that one cannot understand
its inner workings.

Some of the problems with black box models include:
* incorrect medical data
* subjecting individuals to years of extra prison time due to typographical errors
* poorly designed proprietary models for air quality that have led to public wildfires

### General Principles of Interpretable Machine Learning

1. An interpretable machine learning model obeys a domain-specific set of constraints to allow it to be more easily understood by humans.
These constraints can differ dramatically depending on the domain. A typical interpretable supervised learning setup, with data $$ \{z_i\}_i $$, and models chosen from function class $$ \mathcal{F} $$ is:

    $$
    \min_{f \in \mathcal{F}} \frac{1}{n} \sum{\text{Loss}(f, z_i)} + C \cdot \text{InterpretabilityPenalty(f)}, \text{subject to InterpretabilityConstraint(f)}
    $$

    The goal of these constraints is to make the resulting model $$ f $$ or its predictions more interpretable

2. Despite common rhetoric, interpretable models do not necessarily create or enable trust - they could also enable distrust. They simply allow users to decide whether to trust them i.e they permit a decision of trust, rather than trust itself.

3. Don't assume that one needs to make a sacrifice in accuracy in order to gain interpretability. In fact, interpretability can provide accuracy improvements, but not necessarily the other way around.
Interpretability vs accuracy is, in general, a false dichotomy in machine learning.

4. As part of the full data science process, one should expect both the performance metric and interpretability metric to be iteratively refined.

5. For high stakes decisions, interpretable models should be used if possible, rather than "explained" black box models.
    Interpretable ML is not a subset of Explainable AI (XAI). There are many serious problems with the use of explaining black boxes posthoc, such as:
    * Explanations for those black boxes are often misleading, which leads to misplaced trust in black box models.
    * Black boxes are generally unnecessary, given that their accuracy is generally not better than a well-designed interpretable model

---

### 10 Grand Challenges in Interpretable Machine Learning


#### 1. Optimizing Sparse Logical Models: Decision Trees, Decision Lists, and Decision Sets

Some types of Logical Models include:
* Decision Trees
    * each branch node tests a condition, and each leaf node makes a prediction
* Decision Lists
    * composed of `if-then-else` statements
    * rules are tied in order, and the first rule that is satisfied makes the prediction
* Decision Set (disjunction of conjunctions)
    * an unordered collection of rules, where each rule is a conjunction of conditions
    * $$ \geq 1$$ satisfied conditions $$ \rightarrow $$ positive prediction

Full decision tree optimization is known to be a **NP-complete problem**. Initially, the main approach was greedily creating trees from the top down
and pruning them backwards, but this doesn't optimize any particular performance metric. Nowadays, efforts to optimize the performance metric accuracy include mathematical programming,
stochastic search through the space of trees, and dynamic programming.

There are still many challenges to address in efforts to further optimize such as:
1. Improving the scalability of optimal sparse decision trees
2. Effictively handle **continuous variables** without dramatically increasing search space
3. Handling constraints without adding layers of complexity and making it more difficult to optimize

#### 2. Optimization of Scoring Systems


#### 3. Placing Constraints into Generalized Additive Models to Encourage Sparsity and Better Interpretability


#### 4. Modern Case-Based Reasoning


#### 5. Complete Supervised Disentanglement of Neural Networks


#### 6. Complete or Partial Unsupervised Disentanglement of Neural Networks


#### 7. Dimensionality Reduction for Data Visualization


#### 8. Machine Learning Models That Can Incorporate Physics and Other Generative or Casual Constraints


#### 9. Characterization of the "Rashoman Set" of Good Models


#### 10. Interpretable Reinforcement Learning