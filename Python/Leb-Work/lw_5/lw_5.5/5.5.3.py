'''
#3. Create an abstract class MLModel with abstract methods:

train()

predict()

Create subclasses LinearRegressionModel and DecisionTreeModel implementing them.

Instantiate both and show how they share the same interface (train(), predict()), even with different implementations.
'''

from abc import ABC, abstractmethod

class MLModel(ABC):
    @abstractmethod
    def train(self, data):
        pass
        
    @abstractmethod
    def predict(self, sample):
        pass

class LinearRegressionModel(MLModel):
    def train(self, data):
        print(f"Training Linear Regression model using mathematical line fitting on: {data}")
        
    def predict(self, sample):
        return f"Linear Regression prediction for {sample}"

class DecisionTreeModel(MLModel):
    def train(self, data):
        print(f"Training Decision Tree model by splitting nodes on: {data}")
        
    def predict(self, sample):
        return f"Decision Tree prediction for {sample}"

# --- Demonstration & Execution ---

models = [LinearRegressionModel(), DecisionTreeModel()]
training_data = [1, 2, 3, 4, 5]
test_sample = 6

print("--- Running unified ML Interface ---")
for model in models:
    # They share the exact same interface call syntax
    model.train(training_data)
    result = model.predict(test_sample)
    print(f"Result: {result}")
    print("-" * 30)
