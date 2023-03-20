# pbix_doc
Reads a pbix file and generates its documentation. 
# Run test 
```python -m unittest discover tests/ -vvv```

# Install 

In Powershell, we open the target folder and execute the following command:
```
git clone https://github.com/dop12/pbix_doc.git
```
Next, we create a virtual environment:
```
python -m venv .\pbix_doc
```
Then, we activate the virtual environment:
```
pbix_doc\Scripts\activate
```
After that, we install the required modules:
```
cd .\pbix_doc
pip install -r requirements.txt
```
Finally, we can run the command on imput file:
```
cd .\pbix_doc
python .\bin\pbix_doc.py --db_id aw_sales
```
