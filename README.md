# pbix_doc

**pbix_doc** is a set of programs for generating documentation from Power BI files (`pbix`).

Click  [here](./tests/output/index.md) to see output examples. 

# Motivation

Documentation is an essential part of any larger data warehouse project. However, manual documentation can be time-consuming and error-prone. Additionally, regular documentation maintenance can be difficult and time-consuming for developers.

To address these issues, I decided to write a set of programs that support the extraction of data directly from Power BI files and then render this information into human-readable documentation.

With **pbic_doc** you can:

* Automatically extract data from Power BI files, so you don't have to spend time on manual work.
* Render data into human-readable documentation that is accurate and up-to-date.
* Supports different documentation formats, including GitHub Markdown, Azure DevOps Markdown*, and Atlasian Confluence*. *Will be implemented in the future

# Installation

## Prerequisites
You'll need to install 
* Python 3: [https://www.python.org/downloads/](https://www.python.org/downloads/) (developed and tested on version 3.10.7)
* Analysis Services client library ADOMD - [see documentaion here](https://learn.microsoft.com/en-us/analysis-services/client-libraries?view=asallproducts-allversions) it is necessary for [python pyadomd library](https://pypi.org/project/pyadomd/)
* `venv` python module (optional): [https://docs.python.org/3/library/venv.html#module-venv](https://docs.python.org/3/library/venv.html#module-venv) 
* Power BI desktop: [https://aka.ms/pbidesktopstore](https://aka.ms/pbidesktopstore)

## Limitations

The extractor only works on Windows 10/11 due to the use of Power BI Desktop.

## Instalattion steps
1. In Powershell, we open the target folder and execute the following commands:
```
mkdir pbix_doc

cd pbix_doc

git clone https://github.com/dop12/pbix_doc.git
```
2. Next, we create a virtual environment:
```
python -m venv .\pbix_doc.venv
```
3. Then, we activate the virtual environment:
```
.\pbix_doc.venv\Scripts\activate
```
4. After that, we install the required modules:
```
cd .\pbix_doc
pip install -r requirements.txt
```
5. Find out where `AnalysisServicesWorkspaces` folder is and put the path to conf file `.\conf\pbix_doc.yaml`
AnalysisServicesWorkspaces is ussually at on of the these paths `%USERPROFILE%\Microsoft\Power BI Desktop Store App\AnalysisServicesWorkspaces` or `%USERPROFILE%\AppData\Local\Microsoft\Power BI Desktop SSRS\AnalysisServicesWorkspaces`. Power BI Desktop stores local SSAS instance of each open PBIX files.  
```
# edit file .\conf\pbix_doc.yaml and put path into this key local_ssas_folder
local_ssas_folder: "%USERPROFILE%\\Microsoft\\Power BI Desktop Store App\\AnalysisServicesWorkspaces"
```
6. Check that the path to the ADOMD library in `pbix_doc.yaml` is correct. If not, you need to find out where the `Microsoft.AnalysisServices.AdomdClient.dll` library is stored. Sometimes it is stored in the installation subpaths of SSMS, Power BI or Excel. Then update the path in the configuration file.
```
# edit file .\conf\pbix_doc.yaml and put path into this key local_ssas_folder
# Fill path for ADOMD library. See 
# https://learn.microsoft.com/en-us/analysis-services/client-libraries?view=asallproducts-allversions
# or FAQ https://pypi.org/project/pyadomd/
adomd_path: 'C:\\Program Files (x86)\\Microsoft SQL Server Management Studio 18\\Common7\\IDE'
```




## Usage

After installing the program, you can use it to generate documentation for your DWH projects. 

Follow these steps:

1. Open the PBIX files you want to document in Power BI Desktop.

    You can use the test files in the `.\tests\input\` directory, for example.
   
    For this example, we will use `.\tests\input\Life expectancy v202009.pbix`.

2. Open a PowerShell terminal and navigate to the directory where pbix_doc is installed.

```
cd .\pbix_doc
```

3. Run the metadata extraction script. By default, the data is saved to the `./data.json` file, but you can change this with the `--out_file` switch.
```
python .\bin\pbix_doc_extractor.py --out_file .\mydata.json
...
...
2024-01-02 22:42:47.821 INFO     lib.tools  Data saved to ././mydata.json successfully.
2024-01-02 22:42:47.821 INFO     __main__   Done. It took 0h 00m 54s
```
4. Verify the generated json file.
```
dir .\mydata.json

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        02.01.2024     22:42       16068680 mydata.json

```

5. Create a directory for the output documentation.

```
mkdir .\output
```
6. Select the desired documentation format with the `--format` switch, the JSON files you want to generate documentation for with the `--files` switch (--files switch can accept a list of JSON files), and the output directory with the `--out_dir` switch. Then, run the documentation generator.
```
python .\bin\pbix_doc_writer.py --files ./mydata.json --format md_github --out_dir .\output\
...
...
... wrote .\output\Life expectancy v202009.pbix.md
... wrote .\output\index.md
```

7. Verify the generated files.
```
dir .\output\

    Directory: C:\prog\pbix_doc\pbix_doc\output

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        02.01.2024     23:08            396 index.md
-a----        02.01.2024     23:08          72030 Life expectancy v202009.pbix.md
```
8. You can see examples of the generated files [here](./tests/output/index.md) 

8. Then you can commit the files to your documentation repository ( isn't part of this tutorial) and share them with your colleagues.

> [!WARNING]
> **Use of the program is at your own risk.**
>
> The program is still under development and may contain bugs.  If you encounter any problems, please let me know.


