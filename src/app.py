import streamlit as st
import time
import os

from utils import (
    load_config,
    download_proxy,
    get_webdriver,
    get_webdriver_via_proxy,
    get_title_from_link,
    save_book_content_to_docx,
)
from project_dirs import PROJECT_DIR, OUTPUT_DIR

def main():

    st.title("Oreilly Book Downloader")

    # Description of the app
    st.markdown("This app allows you to download books from Oreilly.")
        
    # Input field for book links
    book_links = st.text_area(
        "Enter the links of the books here, separated by comma:",
        height=100,
        )
    book_links_list = book_links.split(',')
    book_links_list = [i.strip().replace('\n', '') for i in book_links_list]

    use_proxy = st.checkbox("Use Proxy")

    cnf = load_config(cnf_dir=PROJECT_DIR, cnf_name="config.yml")
    sleep_time = cnf['login_sleep_time']
    
    # Button to trigger book download
    if st.button("Download Books"):

        if use_proxy:
            proxy = download_proxy(proxy_url=cnf["url_proxy"])
            try:
                driver = get_webdriver_via_proxy(proxy_address=proxy)
            except:
                driver = get_webdriver(chromedriver_path=cnf['chromedriver_path'])
            proxies = {'http': proxy, 'https': proxy}
        else:
            try:
                driver = get_webdriver_via_proxy(proxy_address=proxy)
            except:
                driver = get_webdriver(chromedriver_path=cnf['chromedriver_path'])
            proxies = None

        driver.get("https://learning.oreilly.com/library/view/introduction-to-machine/9781449369880/preface01.html")

        st.info("Remaining time to finish login, after which download will start automatically:")
        progress_bar = st.progress(sleep_time)
        for i in range(sleep_time, -1, -1): 
            progress_bar.progress(i/sleep_time)
            time.sleep(1)
        
        if use_proxy:
            os.environ["HTTPS_PROXY"] = proxy
            
        try:
            for book_url in book_links_list:
                # Open a new tab (this opens a blank page by default)
                driver.execute_script("window.open('', '_blank');")
                driver.switch_to.window(driver.window_handles[1])
                driver.get(book_url)
                time.sleep(1)

                book_title = get_title_from_link(book_url)

                # Get book texts and save them as docx
                save_book_content_to_docx(
                    driver=driver,
                    file_name=book_title,
                    proxies=proxies,
                    common_dir=OUTPUT_DIR,
                    )
                
                st.success(f'Book "{book_title}" saved successfully!')

                # Close the first tab that was opened previously
                driver.switch_to.window(driver.window_handles[0])
                driver.close()

                # Switch back to the new tab
                driver.switch_to.window(driver.window_handles[0])

            st.success("All books downloaded successfully!")

        except Exception as e:
            st.error(f"Error downloading the book: {str(e)}. Please retry.")

        driver.quit()

if __name__ == "__main__":
    main()
