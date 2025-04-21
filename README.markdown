# Internship Recommendation System using RL

This project is a Streamlit-based web application that recommends internships to users by analyzing their resumes. It leverages natural language processing (NLP) with spaCy to extract skills and experience, combined with reinforcement learning (RL) to suggest relevant internships from a predefined dataset. The system aims to streamline the process of finding internship opportunities tailored to a user's profile.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.6 or higher**: The project relies on Python and its package ecosystem.
- **pip**: The Python package manager, typically included with Python.
- **Virtual environment (optional but recommended)**: To keep dependencies isolated.

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/internship-recommendation-system.git
   ```

   Replace `yourusername` with your GitHub username.

2. **Navigate to the Project Directory**

   ```bash
   cd internship-recommendation-system
   ```

3. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. **Install Required Packages**Ensure you have a `requirements.txt` file with the following dependencies:

   ```
   streamlit
   pandas
   numpy
   spacy
   nltk
   pyresparser
   ```

   Then run:

   ```bash
   pip install -r requirements.txt
   ```

6. **Download the spaCy Model**The app uses the `en_core_web_md` model for better similarity computations:

   ```bash
   python -m spacy download en_core_web_md
   ```

   Note: The provided `app.py` currently loads `en_core_web_sm`. For consistency with the notebook and improved performance, update `nlp = spacy.load("en_core_web_sm")` to `nlp = spacy.load("en_core_web_md")` in `app.py`.

## Running the Application

Once the setup is complete, you can launch the app:

1. **Ensure the Virtual Environment is Activated**If not already active, activate it using the commands from step 4 above.

2. **Verify Required Files**Ensure `recomm_df.csv` (internship dataset) and `q_table.npy` (precomputed Q-table) are in the project directory. These files are critical for the app to function.

3. **Update File Paths in** `app.py`The original code uses a Colab-specific path (`/content/recomm_df.csv`). Modify the `dataset` variable in the `main()` function of `app.py`:

   ```python
   dataset = 'recomm_df.csv'
   ```

4. **Run the Streamlit App**

   ```bash
   streamlit run app.py
   ```

5. **Access the App**Open your web browser and navigate to `http://localhost:8501`. You should see the app interface.

## Usage

1. **Upload Your Resume**

   - On the app’s homepage, use the file uploader to submit your resume in **PDF format**.
   - The system processes only PDF files, as specified in the code.

2. **View Recommendations**

   - After processing, the app displays a list of recommended internships, including Job ID, Job Title, Similarity Score, and required Skills.
   - Recommendations are generated based on the precomputed Q-table and similarity between your resume and internship details.

## Project Structure

- `app.py`: The main Streamlit application script.
- `requirements.txt`: List of Python dependencies.
- `recomm_df.csv`: Dataset containing internship details.
- `q_table.npy`: Precomputed Q-table from reinforcement learning.
- `Final_RL_Project (2).ipynb`: Jupyter notebook detailing the RL training process (optional reference).

## Notes and Limitations

- **Precomputed Q-Table**: The current implementation uses a static `q_table.npy` file, meaning recommendations are based on a generic model rather than being fully personalized for each user. For a personalized Q-table, refer to the notebook and compute it separately.
- **File Dependencies**: Ensure `recomm_df.csv` and `q_table.npy` are present in the root directory. Missing files will cause the app to fail.
- **Performance**: The similarity computation uses `en_core_web_md` for better accuracy, but you can revert to `en_core_web_sm` for faster processing if needed (update `app.py` accordingly).
- **Optional Q-Table Computation**: To generate a personalized Q-table, use `Final_RL_Project (2).ipynb`:
  1. Place your resume PDF in the project directory.
  2. Update the resume path in the notebook.
  3. Run the notebook to generate a new `q_table.npy`.

## Contributing

Feel free to fork this repository, submit issues, or send pull requests with improvements. Suggestions for enhancing personalization or optimizing performance are welcome!

## License

This project is open-source and available under the MIT License. (Add a `LICENSE` file to your repo if you choose to include this.)
