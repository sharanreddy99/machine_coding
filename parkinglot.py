from uuid import uuid4
import types

def startParkingSystem():
    print("Welcome to parking lot application.")
    while True:
        inputStr = input()
        if inputStr == "exit":
            print("Closing the app now.")
            return
        
        params = inputStr.split()
        validFunctions = validOptions
        idx = 0
        while idx < len(params):
            if isinstance(validFunctions[params[idx]],dict):
                validFunctions = validFunctions[params[idx]]
            elif isinstance(validFunctions[params[idx]],types.FunctionType):
                validFunctions[params[idx]](*params[idx+1:])
                break
            else:
                print('Invalid option selected. Please try again')
                break
            idx += 1
    
def createParkingLot(id, no_of_floors, no_of_slots):
    global currentLotId
    no_of_floors, no_of_slots = int(no_of_floors),int(no_of_slots)
    parkinglots[id] = {floor: {} for floor in range(no_of_floors)}
    parkinglots[id]["floor_limit"] = no_of_floors
    parkinglots["slots_limit"] = no_of_slots
    initializeCategoryLimit(id, no_of_slots)
    currentLotId = id
    
def setCurrentParkingLot():
    global currentLotId
    while True:
        id = input("Enter parking lot id to use: ")
        if id not in parkinglots:
            print('Parking lot doesnt exist. Please choose a valid id')
        else:
            currentLotId = id
            break

def initializeCategoryLimit(id, no_of_slots):
    global categoryLimit
    categoryLimit[id] = {}
    rem_limit = no_of_slots
    while True:
        if rem_limit == 0:
            break

        name, limit = input("Enter the vehicle category name and limit (Choose * as limit if want to allocate rest of them): ").split()
        print()
        name = name.upper()
        if limit == '*':
            categoryLimit[id][name] = rem_limit
            limit = 0
            break
        else:
            limit = int(limit)
            if limit <= rem_limit:
                rem_limit -= limit
                categoryLimit[id][name] = limit
            else:
                print('Slot limit exceeded. Choose a lesser limit')
        if rem_limit > 0:
            print('Remaining slot count is: ',rem_limit)
    intializeFloorWithSlots(id,no_of_slots)
    print('Parking lot with id:',id,'created successfully.')    

def intializeFloorWithSlots(id,no_of_slots):
    global parkinglots
    for floor in range(parkinglots[id]["floor_limit"]):
        start = 1
        for category in categoryLimit[id]:
            count = categoryLimit[id][category]
            parkinglots[id][floor][category] = {}
            parkinglots[id][floor][category]["free"] = {idx: None for idx in range(start,start+count)}
            parkinglots[id][floor][category]["occupied"] = {}
            start += count

def parkVehicle(vehicleType,vehicleId,color):
    global parking_strategy,currentLotId

    vehicleType = vehicleType.upper()
    if categoryLimit[currentLotId].get(vehicleType) is None:
        print('Invalid vehicle type. Choose one from: ',list(categoryLimit[currentLotId].keys()))
        return
    
    if parking_strategy == 'fifo':
        parkVehicleInFifo(vehicleType,vehicleId,color)

def placeVehicle(vehicleType,floor,vehicleId,color):
    global currentLotId
    id = min(parkinglots[currentLotId][floor][vehicleType]["free"].keys())
    del parkinglots[currentLotId][floor][vehicleType]["free"][id]
    parkinglots[currentLotId][floor][vehicleType]["occupied"][id] = {
        "vehicleId": vehicleId,
        "color": color
    }
    return id

def generateTicket(floor,slot):
    global currentLotId
    ticketid = '{0}_{1}_{2}'.format(currentLotId,floor,slot)
    print('Parked vehicle. Ticket ID:',ticketid)

def parkVehicleInFifo(vehicleType,vehicleId,color):
    global currentLotId
    
    for floor in range(parkinglots[currentLotId]["floor_limit"]):
        if len(parkinglots[currentLotId][floor][vehicleType]["free"]) > 0:
            slot = placeVehicle(vehicleType,floor,vehicleId,color)
            generateTicket(floor, slot)
            break
    else:
        print('Parking Lot Full')

def unparkVehicle(ticketid):
    parts = ticketid.split('_')
    if len(parts) != 3:
        print('Invalid Ticket')
        return
    
    lotid,floor,slot = parts[0],int(parts[1]),int(parts[2])

    if lotid not in parkinglots:
        print('Invalid Ticket')
    elif floor not in parkinglots[lotid]:
        print('Invalid Ticket')
    else:
        for category in parkinglots[lotid][floor]:
            vehicleDetails = parkinglots[lotid][floor][category]["occupied"].get(slot)
            if vehicleDetails != None:
                del parkinglots[lotid][floor][category]["occupied"][slot]
                parkinglots[lotid][floor][category]["free"][slot] = True
                print('Unparked vehicle with Registration Number: {0} and Color: {1}'.format(vehicleDetails["vehicleId"],vehicleDetails["color"]))
                break
        else:
            print('Invalid Ticket')

def freeCount(vehicleType):
    vehicleType = vehicleType.upper()
    global currentLotId
    if categoryLimit[currentLotId].get(vehicleType) is None:
        print('Invalid vehicle type. Please choose one from: ',list(categoryLimit[currentLotId].keys()))
        return
    for floor in range(parkinglots[currentLotId]["floor_limit"]):
        print('No. of free slots for {0} on Floor {1}: {2}'.format(vehicleType,floor,len(parkinglots[currentLotId][floor][vehicleType]["free"])))
    print()
    
def freeSlots(vehicleType):
    vehicleType = vehicleType.upper()
    global currentLotId
    if categoryLimit[currentLotId].get(vehicleType) is None:
        print('Invalid vehicle type. Please choose one from: ',list(categoryLimit[currentLotId].keys()))
        return
    for floor in range(parkinglots[currentLotId]["floor_limit"]):
        print('Free slots for {0} on Floor {1}: {2}'.format(vehicleType,floor,list(parkinglots[currentLotId][floor][vehicleType]["free"].keys())))
    print()

def occupiedSlots(vehicleType):
    vehicleType = vehicleType.upper()
    global currentLotId
    if categoryLimit[currentLotId].get(vehicleType) is None:
        print('Invalid vehicle type. Please choose one from: ',list(categoryLimit[currentLotId].keys()))
        return
    for floor in range(parkinglots[currentLotId]["floor_limit"]):
        print('Occupied slots for {0} on Floor {1}: {2}'.format(vehicleType,floor,list(parkinglots[currentLotId][floor][vehicleType]["occupied"].keys())))
    print()

# variables
parkinglots = {}
categoryLimit = {}
currentLotId = None
parking_strategy = 'fifo'
validOptions = {
    "create_parking_lot": createParkingLot,
    "display": {
        "free_count": freeCount,
        "free_slots": freeSlots,
        "occupied_slots": occupiedSlots,
    },
    "park_vehicle": parkVehicle,
    "unpark_vehicle": unparkVehicle
}

if __name__ == '__main__':
    startParkingSystem()
