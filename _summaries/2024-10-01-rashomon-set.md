---
layout: summary
title: "Exploring the Whole Rashomon Set of Sparse Decision Trees"
date: 2024-10-01
giscus_comments: true
bib_id: 2209.08040v2
---

## Bounds For Reducing Search Space
Can help reduce the search space for Rashomon set construction. Every possible tree is grown using dynamic programming, and some of its leaves will have
determined ("fixed") or not yet been determined ("unfixed").


Terminology:
* Training dataset: $$ \{x_i, y_i\}^n_{i=1} $$
* Binary features: $$ x_i \in \{0, 1\}^p $$
* Labels: $$ y_i \in \{0, 1\} $$
* Loss of tree $$t$$ on the training set: $$ \ell(t, x, y) = \frac{1}{n}\sum_{i=1}^n 1[\hat{y_i} \neq y_i]$$


### $$\epsilon$$-Rashomon Set
The set of all trees $$t \in \mathcal{T}$$ with $$\text{Obj}(t, x, y)$$ at most $$\theta_\epsilon$$

$$
R_{set}(\epsilon, t_{\text{ref}}, \mathcal{T}) := \{t \in \mathcal{T}: \text{Obj}(t, x, y) \leq (1+\epsilon) \times \text{Obj}(t_{\text{ref}}, x, y)\}
$$

* $$t_{\text{ref}}$$ = a benchmark model or reference model from $$\mathcal{T}$$
* $$\mathcal{T}$$ = set of binary classification trees

We can set $$\theta_\epsilon := (1+e) \times \text{Obj}(t_{\text{ref}}, x, y)$$ to denote the threshold of the Rashomon set.


### Basic Rashomon Lower Bound
The lower bound of the objective for tree $$t$$

$$
b(t_{\text{fix}}, x, y) := \ell(t_\text{fix}, x, y) + \lambda H_t
$$

```c++
if (b > epsilon_theta) {
    isRashomonSet = false;
}
```

## Storing, Extracting, and Sampling in the Rashomon Set

Model Set Instance (MSI): `<subproblem, objective>` pair
* Leaf MSI: stores the subproblem's prediction and the number of false positives and negatives
* Internal MSI, $$M$$: Map whose keys are the features on which to split the subproblem and values are an array of pairs, which refers to the left and right MSIs whose objectives sum to the value of $$M$$

## Applications of the Rashomon Set

1. **Model Class Reliance (MCR)** provides the range of **variable importance** across the set of **all**-performing models, not just the importance of one variable to one model.
    * $$MCR_-$$ and $$MCR_+$$ denote the lower and upper bounds of this range
    * A feature with large $$MCR_- \rightarrow$$ important to **all**-performing models
    * A feature with small $$MCR_+ \rightarrow$$ unimportant to every well-performing model
2. The Accuracy metric Covers the Balanced Accuracy and F1 metrics, which can be better suited for imbalanced datasets.
3. Determining How Groups of Samples Influence All-Performing Models


### Experiments
**How do we construct the Rashomon set of decision trees of a dataset?**
* Use the R package BART, setting the number of trees in each iteration to 1
* Generate trees from Random Forest, CART, and GOSDT on multiple subsets of the original data

