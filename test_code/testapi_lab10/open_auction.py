# Importing the FastApi class
from fastapi import FastAPI
import uvicorn

# Creating an app object
app = FastAPI()

class Controller:
    def __init__(self):
        self.__list_auction = []

    def open_auction(self, auction_amulet):
        for auction in self.__list_auction:
            if auction.get_auction_amulet() == auction_amulet:
                return "Auction already exists"

        new_auction = Auction(auction_amulet)
        self.__list_auction.append(new_auction)
        return "Auction is added"
            
    def get_auction_info(self):
        return [auction.get_auction_info() for auction in self.__list_auction]
    
    def get_amulet_list(self):
        return [auction.get_auction_amulet() for auction in self.__list_auction]

    def __str__(self):
        return f"Controller with {len(self.__list_auction)} auctions"

class Auction:
    def __init__(self, auctionAmulet):
        self.__auctionAmulet = auctionAmulet
        self.__list_auction_amulet = []

    def get_auction_info(self):
        return {"auctionAmulet": str(self.__auctionAmulet), "auctionAmuletList": self.__list_auction_amulet}

    def add_auction_amulet(self, auction_amulet):
        self.__list_auction_amulet.append(auction_amulet)
        return "success"

    def get_auction_amulet(self):
        return self.__auctionAmulet

    def __str__(self):
        return f"Auction with {len(self.__list_auction_amulet)} amulets"

class InfoAmulet:
    def __init__(self, name, age, types, detail, status, seller):
        self.__name = name
        self.__age = age
        self.__type = types
        self.__detail = detail
        self.__status = status
        self.__seller = seller

    def __str__(self):
        return f"InfoAmulet: {self.__name} ({self.__type})"

class AuctionAmulet(InfoAmulet):
    def __init__(self, name, age, types, detail, status, seller, start_price, end_price, increase_each_time, start_time, end_time, telephone_number):
        super().__init__(name, age, types, detail, status, seller)

        self.__start_price = start_price
        self.__end_price = end_price
        self.__increase_each_time = increase_each_time
        self.__start_time = start_time
        self.__end_time = end_time
        self.__telephone_number = telephone_number

    def __str__(self):
        return f"AuctionAmulet: {super().__str__()}, Start Price: {self.__start_price}, End Price: {self.__end_price}"

# Creating objects for each class
info_amulet = InfoAmulet(name="Amulet1", age=10, types="Type1", detail="Details", status="Available", seller="Seller1")
auction_amulet = AuctionAmulet(
    name="Amulet1",
    age=10,
    types="Type1",
    detail="Details",
    status="Available",
    seller="Seller1",
    start_price=100,
    end_price=200,
    increase_each_time=10,
    start_time="2024-02-20",
    end_time="2024-03-01",
    telephone_number="1234567890"
)
auction = Auction(auction_amulet)
controller = Controller()
result = controller.open_auction(auction_amulet)
auction_info = controller.get_auction_info()

# Printing more meaningful information
print(info_amulet)
print(auction_amulet)
print(auction)
print(controller)
print(result)
print(auction_info)

@app.post('/open_auction/{auction_amulet}')
def open_auction(auction_amulet: str): 
    return controller.open_auction(auction_amulet)

@app.get('/get_amulet_list/')
def get_amulet_list():
    return controller.get_amulet_list()
    
if __name__ == "__main__":
    uvicorn.run("open_auction:app", host="127.0.0.1", port=8000, log_level="info")