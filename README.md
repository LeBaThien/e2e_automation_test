# e2e_automation_test

## Description
This project contains end-to-end tests for web applications using Selenium and Behave.

## Setup Instructions
1. Install dependencies:
    ```bash
    poetry install
    ```

2. Set the environment variable for the browser (optional, default is Chrome):
    ```bash
    export browser=chrome
    ```

3. Run tests:
    ```bash
    behave
    ```

## Usage Guidelines
- Add your feature files in the `features` directory.
- Implement step definitions in the `steps` directory.
- Use page objects in the `pages` directory to interact with web elements.
