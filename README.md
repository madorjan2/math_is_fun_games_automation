# Selenium-Based Sliding Puzzle Solver

This pet project uses Selenium and Python to automatically solve sliding puzzles found on a specific website.
It navigates the webpage, interacts with the puzzle elements, and solves it algorithmically.

## Prerequisites

* **Python 3.x:** Ensure you have Python 3 installed on your system.
* **Selenium:** Install the Selenium library using pip:
    ```bash
    pip install selenium
    ```

## Setup

1.  **Clone the Repository (if applicable):** If you have this code in a Git repository, clone it to your local machine.
2.  **Install Dependencies:** Navigate to the project directory in your terminal and run:
    ```bash
    pip install -r requirements.txt
    ```
    (Assuming you create a `requirements.txt` file with `selenium` in it).

## Usage

1.  **Navigate to the Project Directory:** Open your terminal and go to the directory where you saved the Python files.
2.  **Run the Script:** Execute the main Python script:
    ```bash
    python plumber_game.py
    ```

The script will then:

* Open the specified webpage.
* Handle any initial popups (like cookies).
* Scroll to the bottom of the page (potentially to ensure the iframe is loaded).
* Switch to the game iframe.
* Attempt to remove ads (implementation details are in `utils.py`).
* Continuously solve each level of the puzzle.

## Disclaimer

This project is intended for educational and personal use only. Automating interactions with websites should be done responsibly and in compliance with the website's terms of service. Avoid using this script in a way that could harm the website or its users.
```
