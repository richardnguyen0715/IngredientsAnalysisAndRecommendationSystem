from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np
import pandas as pd
import requests
import time
from tqdm import tqdm

from concurrent.futures import ThreadPoolExecutor, as_completed