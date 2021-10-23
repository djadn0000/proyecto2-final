import pandas as pd
from pandas.core import algorithms
import numpy as np
import pickle
import sklearn.ensemble as ske
from sklearn import cross_validation, tree, linear_model
from sklearn.feature-selection import SelectFromModel
from sklearn.externals import joblib
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confision_matrix

data= pd.read_csv('data.csv', sep='|')
X = data.drop(['Name', 'md5', 'legitimate'],axis=1).values
y = data['legitimate'].values

print('Researching important feature based on %i total features\n' % X.shape[1])

#Feature selection using Trees classifier
fsel = ske.ExtraTreesClassifier().fit(X,y)
model = SelectFromModel(fsel, prefit=True)
X_new = model.trasform(X)
nb_features = X_new.shape[1]

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X_new, y , test_size=0.2)

features =[]

print('%i features identified as important:' % nb_features)

indices = np.argsort(fsel.feature_impotances_)[::-1][:nb_features]
for f in range(nb_features):
    print("%d. feature %s (%f)"% (f+1,data.columns[2+indices[f]], fsel.feature_importances_[indices[f]]))

# xxx: take care of the feature order
for f in sorted(np.argsort(fsel.feature_importances_)[::-1][:nb_features]):
    features.append(data.columns[2+f])

#Algorithm comparison
algorithms = {
    "DecisionTree": tree.DecisionTreeClassifier(max_depth=10),
    "RandomForest": ske.RandomForestForestClassifier(n_estimators=50),
    "GradientBoosting": ske.GradientBoostingClassifier(n_estimators=100),
    "GNB": GaussianNB()
}

results = {}
print("\n Now testing algorithms")
for algo in algorithms:
    clf = algorithms[algo]
    clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)
    print("%s : %f %%" % (algo, score*100))
    results[algo] = score

winner = max (results, key=results.get)
print('\nWinner algorithm is %s with a %f %% success'%(winner, results[winner]*100))

#Save the algorith and the feature list for leater predictions
print('Saving algorithm and fature list in classifier directory...')
joblib.dump(algorithms[winner], 'classifier/classifier.pkl')
open('classifier/features.pkl', 'w').write(pickle.dumps(features))
print('Saved')