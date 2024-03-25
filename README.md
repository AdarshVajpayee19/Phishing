# phishing-website-detection-content-based
This is an End-to-End Machine Learning Project which focuses on phishing websites to classify phishing and legitimate ones. Particularly, We focused on content-based features like html tag based features. You can find feature extraction, data collection, preparation process here. Also, building ML models, evaluating them are available here.

## inputs
- csv files of phishing and legitimate URLs
  - verified_online.csv --> phishing websites URLs from phishtank.org
  - tranco_list.csv --> legitimate websites URLs from tranco-list.eu
  
## general flow
- Use csv file to get URLs
- Send a request to each URL and receive a response by requests library of python
- Use the content of response and parse it by BeautifulSoup module
- Extract features and create a vector which contains numerical values for each feature
- Repeat feature extraction process for all content\websites and create a structured dataframe
- Add label at the end to the dataframes | 1 for phishing 0 for legitimate
- Save the dataframe as csv and structured_data files are ready!
  - Check "structured_data_legitimate.csv" and "structured_data_phishing.csv" files. 
- After obtaining structured data, you can use combine them and use them as train and test data
- You can split data as train and test like in the machine_learning.py first part, or you can implement K-fold cross-validation like in the second part of the same file. We implemented K-fold as K=5.
- Then We implemented five different ML models:
  - Support Vector Machine
  - Gaussian Naive Bayes
  - Decision Tree
  - Random Forest
  - AdaBoost
- You can obtain the confusion matrix, and performance measures: accuracy, precision, recall
- Finally, We visualized the performance measures for all models.
  - Naive Bayes is the best for my case.

## important notes
- features are content-based and need BeautifulSoup module's methods and fields etc So, you should install it.


## dataset
- with your URL list, you can create your own dataset by using data_collector python file.

