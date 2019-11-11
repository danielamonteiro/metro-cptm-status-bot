import requests
import json
import logging
import os

from dotenv import load_dotenv

class AllLinesStatus:
    
    def __init__(self):
        load_dotenv()
        self.line_status_url = os.getenv("LINE_STATUS_SERVICE")
    
    def get_all_lines(self):
        try:
            logging.info("Consulting Line Status Service...")
            all_lines_response = requests.get(self.line_status_url)
            all_lines_status_code = all_lines_response.status_code
            all_lines_status = json.loads(all_lines_response.text)
            logging.info(f"Line Status Code Return: [{all_lines_status_code}]")
            logging.info(f"Line Status Response: {all_lines_status}")
            #TODO: implementar consulta nos outros endpoints quando der erro na consulta
        except Exception as line_status_exception:
            logging.info(f"Exception consulting Line Status Service: {line_status_exception}")
            all_lines_response = "No response"
            all_lines_status_code = "500"

        if all_lines_status:
            return all_lines_status_code, all_lines_status