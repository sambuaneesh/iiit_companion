# Installation Guide

This guide will walk you through the process of setting up the IIIT Companion application on your local machine.

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Git (optional, for cloning the repository)

## Step 1: Clone the Repository

If you have Git installed, you can clone the repository using the following command:

```
git clone https://github.com/your-username/iiit-companion.git
cd iiit-companion
```

Alternatively, you can download the project as a ZIP file from the GitHub repository and extract it to your desired location.

## Step 2: Create a Virtual Environment (Optional but Recommended)

It's a good practice to create a virtual environment for your Python projects. This keeps dependencies required by different projects separate.

```
python -m venv venv
```

Activate the virtual environment:

- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

## Step 3: Install Dependencies

Install the required Python packages using pip:

```
pip install -r requirements.txt
```

This will install all the necessary dependencies, including Streamlit, FastAPI, and other required libraries.

## Step 4: Configuration

Review the `app/config.py` file and adjust any settings if needed. You can modify port numbers, app name, or add any additional configuration parameters here.

## Step 5: Run the Application

To start the IIIT Companion application, run the following command from the project root directory:

```
python run.py
```

This will start all the microservices and launch the Streamlit app for the IIIT Companion Builder.

## Verifying the Installation

After running the application:

1. Open a web browser and navigate to `http://localhost:8501` (or the port specified in your configuration).
2. You should see the IIIT Companion Builder interface.
3. Try creating a custom dashboard by selecting various features and clicking the "Create My IIIT Companion App" button.
4. If a new URL is generated and you can access the custom dashboard, the installation was successful.

## Troubleshooting

If you encounter any issues during the installation process, please refer to the [Troubleshooting](TROUBLESHOOTING.md) guide or open an issue on the GitHub repository.

## Next Steps

Now that you have successfully installed the IIIT Companion app, you can proceed to the [Usage Guide](USAGE.md) to learn how to use and customize the application.
