from urllib import response
import requests

url = "http://andrewbeatty1.pythonanywhere.com/books"


def getallbooks():
    response = requests.get(url)
    return response.json()


def getbookid(id):
    geturl  = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()


def createbook(book):
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


def updatebook(id, bookdiff):
    updateurl = url + "/" + str(id)
    response = requests.put(updateurl, json=bookdiff)
    return response.json()


def deletebook(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()


# Write a program in another file that works out the average book price from all the books on the server
def averageprice():
    response = requests.get(url)
    loaded = response.json()
    GetPrice = ([d["Price"] for d in loaded])
    avgprice = round(sum(GetPrice) / len(GetPrice))
    return avgprice       


if __name__ == "__main__":
    book= {
        'Author':"Al Johnson",
        'Title':"Moonshine",
        "Price": 25
    }
    bookdiff= {
        'Author':"Alex",
        "Price": 10000
    }
    id = 99
    # print(getallbooks())
    # print(getbookid(19))
    # print(createbook(book))
    # print(updatebook(id, bookdiff))
    # print(deletebook(94))
    #averageprice()
    print("Avergage Price for a book is €" + str(averageprice()))