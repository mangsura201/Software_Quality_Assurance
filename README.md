# ************** Online Banking System using Django **************

## Welcome to [Online Banking System]!

### ************** Getting Started **************

### Follow these simple steps to get started with [Online Banking System using Django]:

### Prerequisites
1. Python 3.10 or 3.11 installed on your computer. If not installed, please download and install it from the official Python website.

### Setting Up a Virtual Environment (Optional but Recommended)
2. It is recommended to set up a virtual environment before installing project dependencies to isolate them from your system's Python installation. 
    - You can create a virtual environment using the following command:
        ```
        python -m venv myenv
        ```
    - Activate the virtual environment:
        - On Windows:
            ```
            myenv\Scripts\activate
            ```
        - On macOS and Linux:
            ```
            source myenv/bin/activate
            ```

### Installation
3. Download the project code from the main branch of the repository to your local directory.
    ```
    git clone https://github.com/mangsura201/Software_Quality_Assurance.git
    ```

### Navigate into the project directory.
4. cd [project directory]

### Install all project dependencies using the following command:
5. pip install -r requirements.txt

### Running the Program
6. Once all dependencies are installed, you can run the program using the following command:
    ```
    python manage.py runserver
    ```

7. Open your web browser and navigate to http://localhost:8000/ to access the application.

### Usage
1. Upon running the program, you will be prompted with a home screen.
2. Sign in as an admin or a customer to explore the features and functionalities of the application.

### Unit Testing
1. Open a terminal or command prompt.
2. Navigate to the root directory of your Django project where manage.py is located.
3. Run the following command:
    ```
    python manage.py test
    ```

### Extra feature of Unit Testing if you want
1. You can also generate a more detailed HTML test coverage report by using tools like coverage.
2. Install coverage if you haven't already:
    ```
    pip install coverage
    ```
3. Then you can run your tests with coverage:
    ```
    coverage run manage.py test
    ```
4. And generate an HTML report:
    ```
    coverage html
    ```
