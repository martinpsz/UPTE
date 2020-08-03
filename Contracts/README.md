#Contracts Project

In this project, I aim to improve the user experience of those making use of UPTE contracts. Currently, the contract articles are uploaded as either PDFs or images, which makes reading and search difficult. Below, I document the steps I am taking.

### Step One:

I created a function called "linkretriever.py" to scrape UPTE's website and return metadata for contract articles (i.e. article number, article name, and article link). Once I captured this data, I saved it in a JSON format for further processing in future steps. Each contract was given its own JSON file prepended by the unit.

###Step Two:

For this step, I cycle through each article link to obtain the contract language. Having examined some of the PDFs, I will have to test to see whether the PDF is an image or a PDF file. Then I will pull needed data.

