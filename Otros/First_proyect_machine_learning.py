from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
         
#Conocimiento de los datos de prueba y como estan distribuidos.
iris_dataset = load_iris()
print("Keys of iris_dataset: \n{}".format(iris_dataset.keys()))
#print(iris_dataset['DESCR'][0:] + "\n...")
print("Targes names : {}".format(iris_dataset['target_names']))
print("Feature names : {}".format(iris_dataset['feature_names']))
print("Type of data: {}".format(type(iris_dataset['data'])))
print("Shape of data: {}".format(iris_dataset['data'].shape))
print("First five columns of data:\n{}".format(iris_dataset['data'][:5]))
print("Type of target: {}".format(type(iris_dataset['target'])))
print("Shape of target: {}".format(iris_dataset['target'].shape))
print("Target:\n{}".format(iris_dataset['target']))

X_train, X_test, Y_train, Y_test = train_test_split(iris_dataset['data'], 
                                                    iris_dataset['target'],
                                                    random_state=0)

print("X_train shape: {}".format(X_train.shape))
print("y_train shape: {}".format(Y_train.shape))
print("X_test shape: {}".format(X_test.shape))
print("y_test shape: {}".format(Y_test.shape))
