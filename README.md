# information_theory2
Final project's second section for the Introduction to Theory Course took at the Federal University of Paraíba.

Project description:

This project's segment is about a standard recognizer 's development based on the LZW algorithm. Using a previously labeled database, on the training stage, a model LZW was generated for each category from the selected database.

The database was organized into samples and clasifications utilizing the cross-validation technique. In this technique, for each database category, while selecting all samples, two of them are subctrated, one for training and one for classification; keeping in mind that this selection must be random. The k-nearest neighbors algorithm was used for classification, with the compressed file size as the distance metric and k =1.

While training can be drescribed as generating a dictionary for each database 's category,  classification/testing represents compressing 1 sample (can not be the one used while generating the template) in all templates/dictionaries. During sample test's compression, the dictionary must remain static. The test sample must be assigned to the best compression's model.

Between the suggested database, the ORL Database of Faces was selected, and all 40 available people on data were utilized (considering 10 face photos for each person).
Dictionaries's size = 2*(K), where K can range between 9 and 16.
It also has a function that plots two graphs ( Hit Rate X K / Processing Time X K).

