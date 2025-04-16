## Proposed Flow

First iteration: Classification based on stylometric features

Train first on the 10 features with basic parameters. 
Use random search/grid search for hyper param tuning.
Do k fold cross validation.
Test on test set.
Save best model to compare results in the future, can structure repo however u like.

Second iteration: Feat engineering

Done by versioning dataset (will figure out how)
Add new features 
Do training, testing etc, same loop as above
Save best model

Remove features that do not contribute that much to the dataset.
Do training, testing, save model etc.

Third iteration: Vector/Embeddings

Get vectors/embeddings of model, start with simple one, maybe cbow-w2v
Train model, test, save etc. 

Fourth iteration: Use diff methods to get embeddings

BERT/Roberta 
Train, test, save

Fifth iteration: Combine best stylo model and best embedded model

Train,test,save

Sixth iteration: Final ensemble

Final ensemble of top three models etc, and see results.
