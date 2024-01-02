# pbix_doc
Reads a pbix file and generates its documentation. 

# Motivace pro vznik programu

Dokumentace je nezbytnou součástí každého většího projektu datových skladů (DWH). Manuální dokumentace však může být časově náročná a náchylná k chybám. Navíc pravidelná údržba dokumentace může být pro programátory obtížná a časově náročná.

Abychom vyřešili tyto problémy, rozhodli jsme se napsat sadu programů, které podporují extrakci dat přímo z PBIX souborů a následně tyto informace renderují do lidsky čitelné dokumentace.

Pomocí pbic_doc můžete:
* Automaticky extrahuje data z PBIX souborů, takže nemusíte trávit čas ruční prací.
* Renderuje data do lidsky čitelné dokumentace, která je přesná a aktuální.
* Podporuje různé formáty dokumentace, včetně GitHub Markdown, Azure DevOps Markdown a Atlasian Confluence.


# Instalace
## Předpoklady
* Nainstalovaný [Python 3](https://www.python.org/downloads/) (vyvíjeno a testováno na verzi 3.10.7)
* Modulem [venv](https://docs.python.org/3/library/venv.html#module-venv) (Volitelně)
* [Power BI desktop](https://aka.ms/pbidesktopstore)

## Omezení
Extraktor pracuje jen na systému Windows 10/11 z důvodu použití Power BI Desktop

## Instalační kroky
In Powershell, we open the target folder and execute the following command:
```
mkdir pbix_doc
cd pbix_doc
git clone https://github.com/dop12/pbix_doc.git
```
Next, we create a virtual environment:
```
python -m venv .\pbix_doc.venv
```
Then, we activate the virtual environment:
```
.\pbix_doc.venv\Scripts\activate
```
After that, we install the required modules:
```
cd .\pbix_doc
pip install -r requirements.txt
```
## Nastavení proměných prostředí
```
XXXX
```


# Použití programu

Po instalaci programu jej můžete použít k vytvoření dokumentace pro své projekty DWH. Postupujte podle následujících kroků:
1. Spustě v Power Bi dekstopu PBIX soubory, které chcete zdokumentovat

   Můžete použít například testovací soubory z aresáře `.\tests\input\`.
   Pro tento příklad použije `.\tests\input\Life expectancy v202009.pbix`

3. V Powershell se přesunňte do příslušného adresáře, kde je nainstalován pbix_doc
4. Spusťte skript pro extrakci metadat (defaultně se data ukládají do souboru `./data.json`, zle změnit přepínačem ----out_file) 
```
cd .\pbix_doc

python .\bin\pbix_doc_extractor.py --out_file .\mydata.json

dir .\mydata.json
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        dd.MM.yyyy     hh:mm       16068680 mydata.json

```
4. Není vyberem požadované formát dokumentace pomocí přepínače -XXX


    Vyberte formát dokumentace, který chcete použít.
    Klikněte na tlačítko "Vygenerovat dokumentaci".

Program vygeneruje dokumentaci v zadaném formátu. Dokumentaci můžete poté otevřít v textovém editoru nebo v prohlížeči.








Použití programu na vlastní riziko

Program je stále ve vývoji a může obsahovat chyby. Používání programu je na vlastní riziko. Pokud narazíte na nějaký problém, dejte nám prosím vědět.








# Run test 
```python -m unittest discover tests/ -vvv```

# Install 

