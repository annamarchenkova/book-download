# oreilly-download
Download books from your Oreilly subscription locally to then use texts for summarization, notes, similarity search etc. 
Downloading is done by providing a link to the first apage of the book and then scraping the pages to save the book context (including images) in .docx format. Code snippets formatting is not yet supported. 
Final app is built in streamlit.

## Installation
Install dependencies from requirements.txt. Adjust parameters in config.yml

## Project structure
```
oreilly-download/
|   config.yml
|   README.md
|   requirements.txt
|   
└─── output/
|   
└─── keys/
|   |    proxy_password.txt
|
└─── src/
    |    app.py
    |    utils.py
    |    project_dirs.py

```

- folder `output`: downloaded books in .docx format
- folder `keys`: 
 proxy_password.txt: file .txt with the proxy password
- folder `src`: Code

## config.yml parameters
url_proxy_wpad: str, link to the wpad web page
proxy_ut: str, proxy UT
proxy_psw_file: str, name of the file in keys folder with the proxy password ('proxy_password.txt')
page_url: str, oreilly page to do manual login ("https://learning.oreilly.com/home-new/")
login_sleep_time: int, time in seconds to leave for manual login. (70) After that time scraping starts automatically

# Use
1. Run app.py 
streamlit run app.py
2. Select use_proxy checkbox if you work via proxy and you set up proxy settings in config and proxy_password.txt file
3. enter list of book links (first pages of the books) to download
4. press `Download Books`.
5. Login to your Oreilly account. After a period of time (login_sleep_time parameter in config) downloading starts automatically.






