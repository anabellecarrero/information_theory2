# information_theory2
Second section of the final project for the Introduction to Theory Course took at the Federal University of Paraíba.

Project description:

This project's segment is about a standard recognizer 's development based on the LZW algorithm. Using a previously labeled database, on the training stage, a model LZW was generated for each category from the selected database.

The database was organized into samples and clasifications utilizing the cross-validation technique. In this technique, for each database category, select all samples - 1 for training and 1 for classification; this selection must be random. For classification, the k-nearest neighbors algorithm was used, with k = 1 and compressed file size as the distance metric.

Training can be drescribed as generating a dictionary for each database 's category. A classification/testing represents compressing 1 sample (which was not used in generating the template) in all templates/dictionaries. During sample test's compression, the dictionary must remain static. The test sample must be assigned to the model with the best compression.

The suggested database used was the ORL Database of Faces, and it utilized all 40 available people on data; each person had 10 face photos.
It was also tested with dictionaries's size 2*(K), which K can range between 9 and 16.

