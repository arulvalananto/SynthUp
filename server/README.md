## To activate virutalenv

```
// For Linux
source venv/bin/active
```

## Setup Insturctions

- You (or others) can install the dependencies using the following command:
  ```bash
  pip install -r requirements.txt
  ```
- Remember to keep your requirements.txt file up-to-date as you add or remove dependencies in your project. You can generate the initial requirements.txt file by running:
  ```bash
  pip freeze > requirements.txt
  ```
- To find the version of a Python package, you can use the pip show command. Open your terminal or command prompt and run:
  ```bash
  pip show package_name
  ```
- If you want to find the version of a package without installing it, you can use the pip search command:
  ```bash
  pip search package_name
  ```

## To start application

    ```
    uvicorn main:app --reload
    ```
