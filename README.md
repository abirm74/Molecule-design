<h2 align="left">Project Overview</h2>
    <p align="left"align="left">Welcome to the Molecule Generation and Bioactivity Prediction Streamlit application repository! This project focuses on utilizing chembl datasets filtered by the standard_type "IC50" for three diseases: Breast Cancer, Inflammatory Bowel Disease, and Alzheimer's. The project spans two primary phases: data preparation and modeling.</p>

<h2 align="left">Data Preparation</h2>
    <p align="left">In this phase, we have meticulously handled the data. The key steps involved are:</p>
    <ul align="left">
        <li><strong>Data Import:</strong> We imported the chembl datasets relevant to our three target diseases.</li>
        <li><strong>Data Cleaning:</strong> Extensive data cleaning was performed to ensure data quality and consistency.</li>
        <li><strong>Feature Engineering:</strong> Feature engineering was conducted to extract relevant information from the dataset for modeling purposes.</li>
    </ul>

<h2 align="left">Modeling Phase</h2>
    <p align="left">The modeling phase encompasses two distinct objectives:</p>

<h3 align="left">1. Molecule Generation</h3>
    <p align="left">For the first objective of molecule generation, we explored two deep learning algorithms: Variational Autoencoder (VAE) and MolGann. After thorough evaluation, we selected VAE as the preferred algorithm and applied it to all three datasets.</p>

<h3 align="left">2. Bioactivity Prediction</h3>
    <p align="left">Regarding the second objective of bioactivity prediction, we employed a variety of machine learning algorithms to predict two key aspects:</p>
    <ul align="left">
        <li><strong>PIC50 Value:</strong> Predicting the PIC50 value for bioactivity.</li>
        <li><strong>Bioactivity Class:</strong> Classifying compounds based on their bioactivity.</li>
    </ul>
    <p align="left">We have identified and saved the best-performing model for each dataset, which will be utilized when deploying the application using Streamlit.</p>

  <h2 align="left">Usage</h2>
    <p align="left">Follow these steps to explore the Molecule Generation and Bioactivity Prediction Streamlit application:</p>
    <ol align="left">
        <li>Clone or download this repository to your local environment.</li>
        <li>Set up the required dependencies and libraries.</li>
        <li>Run the Streamlit application.</li>
        <li>Utilize the application to generate molecules and make bioactivity predictions for the selected diseases.</li>
    </ol>

  <h2 align="left">Dependencies</h2>
    <p align="left">To run this project, you will need the following dependencies:</p>
    <ul align="left">
        <li>Python libraries for data manipulation, modeling, and Streamlit application development.</li>
        <li>Jupyter Notebook (optional for exploring data preprocessing and model development).</li>
        <li>Streamlit (for deploying and running the application).</li>
    </ul>

   <h2 align="left">Future Improvements</h2>
    <p align="left">This project can be extended and improved in various ways:</p>
    <ul align="left">
        <li>Incorporating additional datasets to expand the scope of analysis and prediction.</li>
        <li>Enhancing the user interface and experience of the Streamlit application.</li>
        <li>Implementing more advanced machine learning and deep learning techniques for better prediction accuracy.</li>
        <li>Automating data updates and model retraining for real-time predictions.</li>
        <li>Collaborating with domain experts to further refine the bioactivity prediction models.</li>
    </ul>

  <h2 align="left">Acknowledgments</h2>
    <p align="left">We would like to acknowledge the contribution of the chembl database for providing the dataset used in this project.</p>

