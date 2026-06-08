# Interview Report

**Domain:** deep learning

**Score:** 3/5

**Percentage:** 60.00%

**Generated:** 2026-06-08 14:51:29.395406

---

## Question 1

In deep learning, what is the primary advantage of using the Swish activation function over ReLU?

Your Answer: A

Correct Answer: A

Explanation: Swish (x * sigmoid(x)) is smooth and non-monotonic, allowing small negative values to flow through, reducing the dying neuron issue common with ReLU.

---

## Question 2

Which of the following best describes the role of the temperature parameter in the softmax function commonly used in deep learning?

Your Answer: A

Correct Answer: A

Explanation: The temperature parameter scales the logits before softmax; higher temperatures produce softer, more uniform distributions, while lower temperatures make the distribution sharper and more confident.

---

## Question 3

A deep learning model trained on a large dataset of images achieves 99% accuracy on the training set but only 82% on the test set. Which technique is most directly intended to address this discrepancy?

Your Answer: D

Correct Answer: A

Explanation: The model is overfitting (high training accuracy, lower test accuracy). Dropout randomly drops units during training to reduce co-adaptation, acting as a regularizer to improve generalization.

---

## Question 4

In the context of training deep neural networks, what is the primary function of gradient clipping?

Your Answer: B

Correct Answer: B

Explanation: Gradient clipping is used to avoid the exploding gradient problem, where large gradients can cause unstable updates, by scaling them down if they exceed a set norm or value.

---

## Question 5

In the context of deep learning, what is the primary benefit of using layer normalization over batch normalization in recurrent neural networks (RNNs)?

Your Answer: C

Correct Answer: A

Explanation: Layer normalization normalizes across the feature dimension for each individual sample, independent of the batch size. This makes it particularly suitable for RNNs, where sequence lengths vary and batch statistics can be unreliable during inference or online learning.

---

