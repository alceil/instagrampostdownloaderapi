import requests
from flask import Flask, request, Response
from bs4 import BeautifulSoup
import urllib
from flask_restful import Resource, Api, reqparse
from selenium import webdriver
DRIVER_PATH = 'C:\path\chromedriver'
# url = "https://www.instagram.com/p/B2bFTb-ltz4/"
header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"}
parser = reqparse.RequestParser()
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/upload', methods=['POST'])
def getLink():
    # url = request.form.get('url')
    parser.add_argument("url")
    args = parser.parse_args()
    url = args['url']
    print(url)
    respone=requests.get(url,headers=header)
    soup = BeautifulSoup(respone.text,'html.parser')
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get(url)
    posts = []
    links = driver.find_elements_by_tag_name('img')
    for link in links:
        post = link.get_attribute('src')
        posts.append(post)
    igurl = dict()
    igurl['url'] =  posts[1]   
    print(igurl)
    return igurl





