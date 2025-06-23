from playwright.sync_api import sync_playwright
import time

def get_jobs(job_title):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        search_url = f"https://www.glassdoor.com.br/Job/jobs.htm?sc.keyword={job_title.replace(' ', '+')}"
        print(f"🔗 Acessando: {search_url}")

        page.goto(search_url, timeout=60000)
        time.sleep(5) 
        job_links = page.locator('a.jobLink').all()
        job_descriptions = []

        for idx, job in enumerate(job_links[:10]):
            href = job.get_attribute('href')
            if not href:
                continue

            job_url = "https://www.glassdoor.com.br" + href
            job_page = context.new_page()
            job_page.goto(job_url, timeout=60000)
            time.sleep(3) 

            try:
                description_element = job_page.locator('div.jobDescriptionContent')
                description = description_element.inner_text(timeout=5000)
            except Exception as e:
                description = "Descrição não encontrada."
                print(f"Erro ao obter descrição da vaga {idx+1}: {e}")

            job_descriptions.append(description)
            job_page.close()
            time.sleep(2) 

        browser.close()
        return job_descriptions
