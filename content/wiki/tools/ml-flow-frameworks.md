---
title: "Some ML Workflow Frameworks"
description: "Managing workflows in machine learning projects is not trivial."
date: 2021-01-13
category:
  - "Tools"
tags:
  - "Machine Learning"
  - "Workflow"
references:
  - name: "Built-in magic commands for Jupyter"
    link: https://ipython.readthedocs.io/en/stable/interactive/magics.html
  - name: AWS Cloudwatch
    link: https://aws.amazon.com/cloudwatch/
weight: 6
links:
  - "blog/data-science/a-simple-machine-learning-framework.md"
---


## Metaflow

[Docs](https://docs.metaflow.org/metaflow/client)

A framework for jupyter notebook data scientists.

- Work locally on notebooks.
- Python environment management using conda.
- Work in the cloud with Sagemaker.


|   Tasks    |         Methods          |                                   Comments                                    |
|:----------:|:------------------------:|:-----------------------------------------------------------------------------:|
|    Code    | Scripts/Jupyter Notebook |                                                                               |
| Datastore  |        local + S3        |                                  metaflow.S3                                  |
|  Compute   |    local + AWS Batch     |                                                                               |
|  Metadata  |     metaflow service     | Metadata specifies flow executions: Flows, Runs, Steps, Tasks, and Artifacts. |
| Scheduling |    AWS Step Functions    |                                                                               |
| Deployment |           AWS            |                                                                               |


### Demo

```python
from metaflow import FlowSpec, step

class BranchFlow(FlowSpec):

    @step
    def start(self):
        self.next(self.a, self.b)

    @step
    def a(self):
        self.x = 1
        self.next(self.join)

    @step
    def b(self):
        self.x = 2
        self.next(self.join)

    @step
    def join(self, inputs):
        print('a is %s' % inputs.a.x)
        print('b is %s' % inputs.b.x)
        print('total is %d' % sum(input.x for input in inputs))
        self.next(self.end)

    @step
    def end(self):
        pass

if __name__ == '__main__':
    BranchFlow()
```

## BentoML

[Docs](https://docs.bentoml.org/en/latest/concepts.html)

Make the model ready to serve as an API.
- Easy to get started.
- Great UI to inspect the flow.
- Create API with model artifacts directly in the workflow.
- Supports popular frameworks.
- Creates Dockerfile for serving the model.
- Model can also be distributed as a pypi package.


|   Tasks    |         Methods          |            Comments            |
|:----------:|:------------------------:|:------------------------------:|
|    Code    | Scripts/Jupyter Notebook |                                |
| Datastore  |          local           | Can be packed in Docker Images |
|  Compute   |          local           |       Can be dockerized        |
|  Metadata  |         as file          |  Mostly about model metadata   |
| Scheduling |           None           |                                |
| Deployment |          Docker          |                                |



### Demo

```python
from sklearn import svm
from sklearn import datasets

clf = svm.SVC(gamma='scale')
iris = datasets.load_iris()
X, y = iris.data, iris.target
clf.fit(X, y)

# Create a iris classifier service with the newly trained model
iris_classifier_service = IrisClassifier()
iris_classifier_service.pack("model", clf)

# Test invoking BentoService instance
iris_classifier_service.predict([[5.1, 3.5, 1.4, 0.2]])

# Save the entire prediction service to file bundle
saved_path = iris_classifier_service.save()
```



## ZenML

ZenML is more of an ML framework than a workflow framework.

![High Level Conceptual Diagram of a training pipeline in a ZenML repository](../assets/zenml-architecture.svg)

|   Tasks    |           Methods            |                       Comments                        |
|:----------:|:----------------------------:|:-----------------------------------------------------:|
|    Code    |           Scripts            |                Mostly tensorflow-based                |
| Datastore  | local + google cloud storage |                                                       |
|  Compute   |         local + k8s          | e.g., Google Cloud Dataflow, Google Cloud AI Platform |
|  Metadata  |           as file            |              Mostly about model metadata              |
| Scheduling |             None             |                                                       |
| Deployment |   Google Cloud AI Platform   |                                                       |




### Demo


```python
from zenml.core.datasources.csv_datasource import CSVDatasource
from zenml.core.pipelines.training_pipeline import TrainingPipeline
from zenml.core.steps.evaluator.tfma_evaluator import TFMAEvaluator
from zenml.core.steps.preprocesser.standard_preprocesser.standard_preprocesser import StandardPreprocesser
from zenml.core.steps.split.random_split import RandomSplit
from zenml.core.steps.trainer.feedforward_trainer import FeedForwardTrainer

training_pipeline = TrainingPipeline(name='Quickstart')

# Add a datasource. This will automatically track and version it.
ds = CSVDatasource(name='Pima Indians Diabetes Dataset',
                   path='gs://zenml_quickstart/diabetes.csv')
training_pipeline.add_datasource(ds)

# Add a random 70/30 train-eval split
training_pipeline.add_split(RandomSplit(split_map={'train': 0.7, 'eval': 0.3}))

# StandardPreprocesser() has sane defaults for normal preprocessing methods
training_pipeline.add_preprocesser(
    StandardPreprocesser(
        features=['times_pregnant', 'pgc', 'dbp', 'tst', 'insulin', 'bmi',
                  'pedigree', 'age'],
        labels=['has_diabetes'],
        overwrite={'has_diabetes': {
            'transform': [{'method': 'no_transform', 'parameters': {}}]}}
    ))

# Add a trainer
training_pipeline.add_trainer(FeedForwardTrainer(
    loss='binary_crossentropy',
    last_activation='sigmoid',
    output_units=1,
    metrics=['accuracy'],
    epochs=20))


# Add an evaluator
training_pipeline.add_evaluator(
    TFMAEvaluator(slices=[['has_diabetes']],
                  metrics={'has_diabetes': ['binary_crossentropy',
                                            'binary_accuracy']}))

# Run the pipeline locally
training_pipeline.run()
```