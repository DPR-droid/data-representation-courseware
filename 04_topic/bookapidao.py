from urllib import response
import requests

url = "http://andrewbeatty1.pythonanywhere.com/books"


def getallbooks():
    response = requests.get(url)
    return response.json()


def getBookId(id):
    geturl  = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()


def createBook(book):
    # book = {
    #         'Author': 'Jonas Jonasson', 
    #         'Price': 123, 
    #         'Title': 'Sweet sweet revenge', 
    #         'id': 1
    #     }
    response = requests.post(url, json = book)
    #headers ={ "Content-type": "application/json"}
    #response = requests.post(url, data=json.dumps(book), headers=headers)
    return response.json


def updateBook(id, bookdiff):
    updateurl = url + "/" + str(id)
    response = requests.put(updateurl, json=bookdiff)
    return response.json()
    pass

def deleteBook(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()
    


if __name__ == "__main__":
    book= {
        'Author':"Al Johnson",
        'Title':"Moonshine",
        "Price": 25.25
    }
    bookdiff= {
        'Author':"Alex",
        "Price": 10000
    }
    id = 99
    # print(getallbooks())
    # print(getBookId(19))
    # print(createBook(book))
    # print(updateBook(id, bookdiff))
    # print(deleteBook(94))